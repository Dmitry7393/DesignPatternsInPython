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