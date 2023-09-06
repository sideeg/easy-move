import sqlite3
from sqlite3 import Error
import sys 


def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


if __name__ == '__main__':
    print(r"/home/ubuntu/easy_move/db/"+sys.argv[1]+".db")
    create_connection(r"/home/ubuntu/easy_move/db/"+sys.argv[1]+".db")

