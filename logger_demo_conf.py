import logging
import logging.config

class LoggingConf():
    def testLog(self):
        # Create Logger
        logging.config.fileConfig('logging.conf')
        logger = logging.getLogger(LoggingConf.__name__)
        # Logging Messages
        logger.debug('debug message')
        logger.info ('info Messages')
        logger.warn('warn message')
        logger.error('error message')
        logger.critical('critical messages')

demo = LoggingConf()
demo.testLog()
