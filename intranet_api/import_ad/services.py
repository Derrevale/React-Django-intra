import json
import os
import time
from typing import Optional

from ldap3 import Server, ALL, Connection, SUBTREE, ALL_ATTRIBUTES, Entry

from import_ad.models import SilvaUser
from intranet_core import settings

ENTRY_KEYS = [
    'sAMAccountName',
    'sn',
    'givenName',
    'mail',
    'st',
]


def find_user(username: str) -> Optional[SilvaUser]:
    from intranet_core.settings import logger
    user = None
    try:
        user = SilvaUser.objects.get(username=username)
    except SilvaUser.DoesNotExist:
        logger.info(f'User {username} not found in the Silva database.')
    return user


def is_entry_a_valid_user(ldap_entry: Entry) -> bool:
    is_valid = True
    for key in ENTRY_KEYS:
        if key not in ldap_entry.entry_attributes_as_dict:
            is_valid = False
            break
    return is_valid


def load_exclusion_list() -> list[str]:
    file_path = os.path.join(settings.PROJECT_ROOT, '..', 'files', 'exclude-emails.json')
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            json_content = json.load(f)
            if 'excludeEmails' in json_content:
                return json_content.get('excludeEmails', [])
    raise Exception('Could not load the exclusion list')


def import_ldap_users() -> dict:
    from intranet_core.settings import logger
    from intranet_core import settings

    start_time = time.time()
    counter = 0
    invalid = 0
    already_existing = 0
    errors = 0

    # Initialize processed_users as a set
    processed_users = set()

    ad_server = Server(settings.AUTH_LDAP_SERVER_URI, use_ssl=False, get_info=ALL)
    ad_connection = Connection(ad_server, user=settings.AUTH_LDAP_BIND_DN,
                               password=settings.AUTH_LDAP_BIND_PASSWORD, auto_bind='DEFAULT')

    if not ad_connection.bind():
        logger.error(f'Error while binding to the Active Directory: {ad_connection.result}')
        raise Exception(ad_connection.result)

    exclusion_list = load_exclusion_list()
    page_size = 100
    cookie = None
    total_entries = 0

    while True:
        ad_connection.search(search_base='ou=SILVA,dc=silva,dc=lan',
                             search_filter='(objectClass=user)',
                             search_scope=SUBTREE,
                             attributes=ALL_ATTRIBUTES,
                             paged_size=page_size,
                             paged_cookie=cookie)

        total_entries += len(ad_connection.response)
        logger.info(f'Found {total_entries} entries in the Active Directory so far...')

        # Loop on the results
        for ad_user in ad_connection.entries:
            try:
                if ad_user.sAMAccountName.value in processed_users:
                    continue

                if 'mail' not in ad_user.entry_attributes_as_dict:
                    continue
                if 'msExchUserAccountControl' in ad_user.entry_attributes_as_dict and ad_user.msExchUserAccountControl.value == 2:
                    continue

                # Check if the user is in the exclusion list
                if 'mail' in ad_user.entry_attributes_as_dict and ad_user.mail.value in exclusion_list:
                    logger.info(f'User {ad_user.sAMAccountName.value} is in the exclusion list. Skipping...')
                    continue

                # Check if the user already exists in the Silva database
                user = find_user(ad_user.sAMAccountName.value)
                is_new = True

                # Check if the entry is a valid user
                if not is_entry_a_valid_user(ad_user):
                    logger.info(f'User {ad_user.sAMAccountName.value} is not a valid user. Skipping...')
                    invalid += 1
                    continue

                if user:
                    logger.info(f'User {ad_user.sAMAccountName.value} already exists in the database.')
                    is_new = False
                else:
                    user = SilvaUser()

                # Create or update the user in the Silva database
                user.username = ad_user.sAMAccountName.value
                user.first_name = ad_user.givenName.value
                user.last_name = ad_user.sn.value
                user.email = ad_user.mail.value
                user.is_staff = False
                user.is_superuser = False
                user.is_active = True
                user.site = ad_user.st.value

                # Check if the user has a phone number
                if 'telephoneNumber' in ad_user.entry_attributes_as_dict:
                    user.phone = ad_user.telephoneNumber.value

                # Set a dummy default password
                user.set_password(f'silva_{ad_user.sAMAccountName.value}')

                # Save the user
                user.save()

                # Add the processed user to the set
                processed_users.add(ad_user.sAMAccountName.value)

                if is_new:
                    logger.info(f'User {ad_user.sAMAccountName.value} created in the database.')
                    counter += 1
                else:
                    logger.info(f'User {ad_user.sAMAccountName.value} updated in the database.')
                    already_existing += 1

            except Exception as e:
                logger.error(f'Error while importing user {ad_user.sAMAccountName}: {e}')
                errors += 1

        logger.info(f'{counter + already_existing} users processed so far...')

        # Handle pagination (get the cookie for the next page)
        cookie = ad_connection.result['controls']['1.2.840.113556.1.4.319']['value'].get('cookie')

        # Exit the loop when there are no more pages
        if not cookie:
            break

    logger.info(
        f'Imported {counter + already_existing} users with {errors} errors in {time.time() - start_time} seconds.')

    return {
        'imported_users': counter,
        'invalid_users': invalid,
        'already_existing_users': already_existing,
        'errors': errors,
    }
