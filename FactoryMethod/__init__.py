import abc
import sqlite3
#import mysql.connector

class Database(metaclass=abc.ABCMeta):

    def __init__(self):
        pass

    @abc.abstractmethod
    def create_database(self):
        pass


class MySqlDatabase(Database):

    def create_database(self):
        print('create MySqlTable')


class SqlLite3Database(Database):

    def create_database(self):
        print('create SqlLiteTable')


class DatabaseFactory(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def create_database(self):
        pass


class MySqlDbFactory(DatabaseFactory):

    def create_database(self):
        print('return MySqlDatabase')
        return MySqlDatabase()


class SqlLite3Factory(DatabaseFactory):

    def create_database(self):
        print('return SqlLite3 database')
        return SqlLite3Database()

def main():
    mysql_db_factrory = MySqlDbFactory()
    mysql_db_factrory.create_database()


if __name__ == "__main__":
    main()