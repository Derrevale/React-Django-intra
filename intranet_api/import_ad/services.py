import time
from typing import Optional

from ldap3 import Server, ALL, Connection, SUBTREE, ALL_ATTRIBUTES, Entry

from import_ad.models import SilvaUser

ENTRY_KEYS = [
    'sAMAccountName',
    'sn',
    'givenName',
    'mail',
    'st',
]


def find_user(username: str) -> Optional[SilvaUser]:
    """
    Finds a user in the Silva database.
    :param username: the username.
    :return: the user if found, None otherwise.
    """

    # Import here to avoid circular imports (and runtime insults)
    from intranet_core.settings import logger

    # Initialize some working variables
    user = None

    # Try to find the user
    try:
        user = SilvaUser.objects.get(username=username)
    except SilvaUser.DoesNotExist:
        logger.info(f'User {username} not found in the Silva database.')

    return user


def is_entry_a_valid_user(ldap_entry: Entry) -> bool:
    """
    Checks if an LDAP entry is a valid user.
    """

    # Import here to avoid circular imports (and runtime insults)

    # Initialize some working variables
    is_valid = True

    for key in ENTRY_KEYS:
        if key not in ldap_entry.entry_attributes_as_dict:
            is_valid = False
            break

    return is_valid


def import_ldap_users() -> dict:
    """
    Import Active Directory users into the Silva database as SilvaUser entities.

    :return: counters and errors.
    """

    # Import here to avoid circular imports (and runtime insults)
    from intranet_core.settings import logger
    from intranet_core import settings

    # Initialize some working variables
    start_time = time.time()
    counter = 0
    invalid = 0
    already_existing = 0
    errors = 0

    # Connect to the Activer Directory
    ad_server = Server(settings.AUTH_LDAP_SERVER_URI, use_ssl=False, get_info=ALL)
    ad_connection = Connection(ad_server, user=settings.AUTH_LDAP_BIND_DN,
                               password=settings.AUTH_LDAP_BIND_PASSWORD, auto_bind='DEFAULT')

    # Bind the connection
    if not ad_connection.bind():
        logger.error(f'Error while binding to the Active Directory: {ad_connection.result}')
        raise Exception(ad_connection.result)

    try:
        # Perform the search
        ad_connection.search(search_base='ou=SILVA,dc=silva,dc=lan',
                             search_filter='(objectClass=user)',
                             search_scope=SUBTREE,
                             attributes=ALL_ATTRIBUTES,
                             get_operational_attributes=True)
    except Exception as e:
        logger.error(f'Error while searching the Active Directory: {e}')
        raise e

    # Loop on the results
    for ad_user in ad_connection.entries:
        try:
            # Check if the user already exists in the Silva database
            user = find_user(ad_user.sAMAccountName.value)
            # Initialize the is_new flag
            is_new = True

            # Check if the entry is a valid user
            if not is_entry_a_valid_user(ad_user):
                # The entry is not a valid user
                logger.info(f'User {ad_user.sAMAccountName.value} is not a valid user. Skipping...')
                invalid += 1
                continue

            if user:
                # The user already exists in the Silva database
                logger.info(f'User {ad_user.sAMAccountName.value} already exists in the database.')
                is_new = False
            else:
                # The user does not exist in the Silva database
                user = SilvaUser()

            # Create the user in the Silva database
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
                # If so, set it
                user.phone = ad_user.phoneNumber.value

            # Set a dummy default password (will not be used for authentication but is mandatory in the database)
            user.set_password(f'silva_{ad_user.sAMAccountName.value}')

            # Save the user
            user.save()

            if is_new:
                # Log the creation
                logger.info(f'User {ad_user.sAMAccountName.value} created in the database.')
                # Increment the counter
                counter += 1
            else:
                # Log the update
                logger.info(f'User {ad_user.sAMAccountName.value} updated in the database.')
                # Increment the counter
                already_existing += 1
        except Exception as e:
            # Log the error
            logger.error(f'Error while importing user {ad_user.sAMAccountName}: {e}')
            # Increment the error counter
            errors += 1

    logger.info(
        f'Imported {counter + already_existing} users with {errors} errors in {time.time() - start_time} seconds.')

    return {
        'imported_users': counter,
        'invalid_users': invalid,
        'already_existing_users': already_existing,
        'errors': errors,
    }
