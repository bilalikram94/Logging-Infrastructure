import logging
from new.custom_logger import customLogger

class LoggingDemo2():
    log = customLogger(logging.DEBUG)
    def method1(self):
        self.log.debug('DEBUG messages')
        self.log.info('INFO messages')
        self.log.warn('Warn messages')
        self.log.error('Error messages')
        self.log.critical('Critical messages')

    def method2(self):
        self.log.debug('DEBUG messages')
        self.log.info('INFO messages')
        self.log.warn('Warn messages')
        self.log.error('Error messages')
        self.log.critical('Critical messages')


    def method3(self):
        self.log.debug('DEBUG messages')
        self.log.info('INFO messages')
        self.log.warn('Warn messages')
        self.log.error('Error messages')
        self.log.critical('Critical messages')


ff = LoggingDemo2()
ff.method1()
ff.method2()
ff.method3()