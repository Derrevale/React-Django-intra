import time

from ldap3 import Server, Connection, ALL


def import_ldap_users():
    """
    Import Active Directory users into the Silva database as SilvaUser entities.
    """

    # Import here to avoid circular imports (and runtime insults)
    from intranet_core.settings import logger
    from intranet_core import settings

    # Initialize some working variables
    start_time = time.time()
    counter = 0
    errors = 0

    # Connect to the Activer Directory
    ad_server = Server(settings.AUTH_LDAP_SERVER_URI, get_info=ALL)
    ad_connection = Connection(ad_server, user=settings.AUTH_LDAP_BIND_DN,
                               password=settings.AUTH_LDAP_BIND_PASSWORD)

    try:
        # Perform the search
        ad_connection.search(search_base='ou=SILVA,dc=silva,dc=lan',
                             search_filter='(objectClass=person)',
                             attributes=['cn', 'givenName', 'sn', 'mail', 'sAMAccountName', 'memberOf'])
    except Exception as e:
        logger.error(f'Error while searching the Active Directory: {e}')
        raise e

    # Loop on the results
    for ad_user in ad_connection.entries:
        try:
            # Create the user in the Silva database
            logger.error(f'Importing user {ad_user.sAMAccountName}...')
            # Increment the counter
            counter += 1
        except Exception as e:
            # Log the error
            logger.error(f'Error while importing user {ad_user.sAMAccountName}: {e}')
            # Increment the error counter
            errors += 1

    logger.info(f'Imported {counter} users with {errors} errors in {time.time() - start_time} seconds.')
