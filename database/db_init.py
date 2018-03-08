"""
Files: db_init.py
    Check database initialization
    @date_modified - 03/08/18
    @author - Elijah Bendinsky
"""
import logging
from database import METADATA

LOGGER = logging.getLogger(__name__)


def database_check_init():
    """
    Methods: database_check_init
        Test that the Postgres connection works, and the proper tables have been added
    Returns:
        None -- posts results to the log
    """
    if 'tournament' in METADATA.tables and 'rule_set' in METADATA.tables and \
            'match' in METADATA.tables and 'team' in METADATA.tables:
        # Report success if everything is gucci
        LOGGER.info("Database exists, and is proper")
    else:
        # Report failure and exit if everything is sad boi
        LOGGER.error("Database does not exist or is not proper")
        exit(1)
