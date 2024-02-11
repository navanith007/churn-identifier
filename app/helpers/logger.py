import logging


def setup_logger():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

    # You can also configure additional settings here, such as logging to a file.


setup_logger()

# Create logger instance to be used in other modules
logger = logging.getLogger(__name__)
