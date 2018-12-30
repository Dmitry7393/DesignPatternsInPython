
class Worker(object):
    def export_data(self, exporter):
        print(self.__class__.__name__.lower())
        method_name = 'export_data_of_{}'.format(self.__class__.__name__.lower())
        print('method_name = ', method_name)
        export = getattr(exporter, method_name)
        return export(self)


class Developer(Worker):

    specific_data_for_developer = 1

    def __init__(self):
        self.work_experience = 1

    def get_type(self):
        return '-- Developer --'


class Tester(Worker):

    specific_data_for_tester = 2

    def __init__(self):
        self.work_experience = 1

    def get_type(self):
        return '-- Tester --'


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


def main():
    xml_exporter = XMLExporter()
    json_exporter = JSONExporter()
    developer = Developer()
    developer.export_data(xml_exporter)

    tester = Tester()
    tester.export_data(json_exporter)


if __name__ == "__main__":
    main()