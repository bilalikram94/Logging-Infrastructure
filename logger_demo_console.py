import logging


class LoggerDemoClass:
    def testlog(self):
        # Create Logger
        logger = logging.getLogger(LoggerDemoClass.__name__)
        logger.setLevel(logging.INFO)

        # Create Console Handler and Set Level Info
        chandler = logging.StreamHandler()
        chandler.setLevel(logging.INFO)

        # Create Formatter
        formatter = logging.Formatter('%(asctime)s-%(name)s -%(levelname)s :%(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

        # Add formatter  to console handler ->ch
        chandler.setFormatter(formatter)

        # Add Console Handler to Logger
        logger.addHandler(chandler)

        # Logging Messages
        logger.debug('DEBUG messages')
        logger.info('INFO messages')
        logger.warn('Warn messages')
        logger.error('Error messages')
        logger.critical('Critical messages')


ff = LoggerDemoClass()
ff.testlog()