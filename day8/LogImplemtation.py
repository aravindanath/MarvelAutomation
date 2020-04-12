# print("Hello is a report")

# https://docs.python.org/3/library/logging.html
import logging

logger = logging.getLogger("Demo log")

fileHandler =logging.FileHandler("logFile.log")

logger.addHandler(fileHandler)

formater = logging.Formatter("%(asctime)s :%(levelname)s: %(name)s :%(message)s")
fileHandler.setFormatter(formater)
logger.setLevel(logging.DEBUG)
logger.debug("=== user is on home page ====")
logger.info("=== user is on search page ====")
logger.critical("=== user is on critical log ===")
logger.warning("=== user is on warinig log ===")
logger.fatal("=== user is on fatal log ===")
logger.error("=== user is on error log ===")

