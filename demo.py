# from src.logger import logging

# logging.debug("this is the debug message")
# logging.info("this is an info message")
# logging.warning("this is an warning message")
# logging.error("this is an error message")
# logging.critical("this is an critical message")
from src.logger import logging
from src.exception import MyException
import sys
try:
    a = 1+'Z'
except Exception as e:
    logging.info(e)
    raise MyException(e, sys) from e