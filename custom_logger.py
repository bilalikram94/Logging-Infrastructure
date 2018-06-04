import inspect
import logging


def customLogger(Loglevel):
    loggerName = inspect.stack()[1][2]
    # logger = logging.getLogger(loggerName)
    logger = logging.getLogger("test")
    logger.setLevel(logging.DEBUG)

    fileHandler = logging.FileHandler("{0}.log".format(loggerName), mode='w')
    fileHandler.setLevel(Loglevel)

    formatter = logging.Formatter('%(asctime)s-%(name)s -%(levelname)s :%(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
    fileHandler.setFormatter(formatter)

    logger.addHandler(fileHandler)

    return logger