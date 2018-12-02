import datetime

class LogManger:
    # Here will be the instance stored.
    __instance = None

    def __init__(self):
        self.path = ""

        if LogManger.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            LogManger.__instance = self

    @staticmethod
    def getLogManager():
        """ Static access method. """
        if LogManger.__instance == None:
            LogManger()
        return LogManger.__instance



    def some_useful_function(self):
        print('this is usefule function')

    def set_folder_for_logs(self, path):
        self.path = path

    def append_to_file(self, data, log_level):
        """Append a string to the file
                   File will be created if it does not exist yet.
                """

        with open(self.path, 'a+', encoding='utf-8') as f:
            f.write(str(datetime.datetime.now()) + ' ' + log_level + ': ' + data)
            f.write('\n')

    def info(self, data):
        self.append_to_file(data, 'INFO')

    def error(self, data):
        self.append_to_file(data, 'ERROR')

    def debug(self, data):
        self.append_to_file(data, 'DEBUG')


logger = LogManger()
logger.set_folder_for_logs('/tmp/logs_my_test_application.log')
logger.info('log1')
logger.error('test2')
logger.debug('test3')

s = LogManger.getLogManager()