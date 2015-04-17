__author__ = 'evanwu'
from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config

def connect():
    """
    Connect to MySQL database
    """

    db_config = read_db_config()

    try:
        print 'Connecting to MySQL Database...'
        conn = MySQLConnection(**db_config)

        if conn.is_connected():
            print 'Connection established'
        else:
            print 'Connection failed'

    except Error as e:
        print(e)

    finally:
        conn.close()
        print 'Connection Closed'

if __name__=='__main__':
    connect()