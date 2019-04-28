import abc


class Database(metaclass=abc.ABCMeta):

    def __init__(self):
        pass

    @abc.abstractmethod
    def info(self):
        pass


class MySqlDatabase(Database):

    def info(self):
        print('MySqlDatabase')


class SqlLite3Database(Database):

    def info(self):
        print('SqlLite3Database')


class PostgreSQLDatabase(Database):

    def info(self):
        print('PostgreSQL')


class DatabaseFactory(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def create_database(self):
        pass


class MySqlDbFactory(DatabaseFactory):

    def create_database(self):
        return MySqlDatabase()


class SqlLite3Factory(DatabaseFactory):

    def create_database(self):
        return SqlLite3Database()


class PostgreSQLFactory(DatabaseFactory):

    def create_database(self):
        return PostgreSQLDatabase()


def main():
    mysql_db_factrory = MySqlDbFactory()
    sqllite3_db_factory = SqlLite3Factory()
    postgre_sql_factory = PostgreSQLFactory()

    database_list = []
    database_list.append(mysql_db_factrory.create_database())
    database_list.append(sqllite3_db_factory.create_database())
    database_list.append(postgre_sql_factory.create_database())

    for database in database_list:
        database.info()


if __name__ == "__main__":
    main()

