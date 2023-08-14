import logging


def get_logger(name):
    format = '%(asctime)s  -  %(name)s  -  %(levelname)s\n%(filename)s --> %(funcName)s'
    logging.basicConfig(format=format)
    logger = logging.getLogger(name)
    return logger
