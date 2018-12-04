import abc


class TableFactory(metaclass=abc.ABCMeta):

    def __init__(self):
        self.product = self._factory_method()

    @abc.abstractmethod
    def _factory_method(self):
        pass

    def some_operation(self):
        self.product.interface()


class MySqlTableFactory(TableFactory):

    def _factory_method(self):
        return MySqlTable()


class OracleTableFactory(TableFactory):

    def _factory_method(self):
        return OracleTable()


class DbTable(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def interface(self):
        pass


class MySqlTable(DbTable):

    def interface(self):
        pass


class OracleTable(DbTable):

    def interface(self):
        pass


def main():
    mysql_table_factory = MySqlTableFactory()
    mysql_table_factory.product.interface()
    mysql_table_factory.some_operation()


if __name__ == "__main__":
    main()