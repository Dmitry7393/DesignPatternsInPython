

class DataExporter(object):
    def __str__(self):
        return self.__class__.__name__


class XMLExporter(DataExporter):

    def export_data_of_developer(self, developer):
        print('create xml file with info about developer', developer.get_type())

    def export_data_of_tester(self, tester):
        print('create xml file with info about tester %d', tester.get_type())

    def export_data_of_manager(self, manager):
        print('create xml file with info about manager')


class JSONExporter(DataExporter):

    def export_data_of_developer(self, developer):
        print('create JSON file with info about developer')

    def export_data_of_tester(self, tester):
        print('create JSON file with info about tester: ', tester.get_type())

    def export_data_of_manager(self, manager):
        print('create JSON file with info about manager')