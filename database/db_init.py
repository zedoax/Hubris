from database import metadata
import logging

logger = logging.getLogger(__name__)


def database_check_init():
    if 'tournament' in metadata.tables and 'rule_set' in metadata.tables and \
            'match' in metadata.tables and 'team' in metadata.tables:
        logger.info("Database exists, and is proper")
    else:
        logger.error("Database does not exist or is not proper")
        exit(1)
