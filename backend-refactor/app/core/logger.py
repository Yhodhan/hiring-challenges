import logging

# Enable the logs in the project 
def setup_logger(log_level):
    logging.basicConfig(
        level=log_level, format="%(asctime)s │ %(levelname)s │ %(name)s - %(message)s"
    )
