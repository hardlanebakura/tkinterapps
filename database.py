import json
import mysql.connector
from mysql.connector.cursor import MySQLCursorPrepared

class Database(object):

    def connect(self):
        return mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "",
            database = "fusioncharts"
        )

    def __init__(self):
        self.con = self.connect()
        self.cursor = self.con.cursor(buffered = True)
        self.cursor1 = self.con.cursor(buffered = True)
        self.cursor_prep = self.con.cursor(cursor_class = MySQLCursorPrepared)

    def select(self, table_name, columns):
        str = ""
        if isinstance(columns, list):
            for column in columns:
                str += column
                if columns.index(column) != len(columns) - 1:
                    str += ", "
        else:
            str = columns
        self.cursor.execute("SELECT {} FROM {}".format(str, table_name))
        return self.cursor.fetchall()

    def select_all(self, table_name):
        self.cursor.execute("SELECT * FROM {}".format(table_name))
        result = self.cursor.fetchall()
        return [item[1:] for item in result]

    def insert_into(self, table_name, columns, values):
        if not isinstance(table_name, str):
            raise TypeError("Expected string input")
        if not isinstance(columns, list):
            raise TypeError("Expected list input")
        if not isinstance(values, list):
            raise TypeError("Expected list input")
        col_names = ""
        col_values = ""
        for column in columns:
            col_names += column
            col_values += "?"
            if columns.index(column) != len(columns) - 1:
                col_names += ", "
                col_values += ", "
        prep_statem = "INSERT INTO {} ({}) VALUES ({})".format(table_name, col_names, col_values)
        self.cursor_prep.execute(prep_statem, values)
        self.con.commit()

    def show(self, table_name):
        self.cursor.execute("SHOW columns FROM {}".format(table_name))
        return [item[0] for item in self.cursor.fetchall()][1:]

    def to_dict(self, table_name):
        self.cursor.execute("SHOW columns FROM {}".format(table_name))
        columns = [item[0] for item in self.cursor.fetchall()][1:]
        self.cursor.execute("SELECT * FROM {}".format(table_name))
        items = [item[1:] for item in self.cursor.fetchall()]
        list1 = []
        for item in items:
            d = {}
            for key in item:
                d[columns[item.index(key)]] = key
            list1.append(d)
        return list1

db = Database()



