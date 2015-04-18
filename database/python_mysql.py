__author__ = 'evanwu'
from mysql.connector import Error, MySQLConnection
from python_mysql_dbconfig import read_db_config


def connect():

    db_config = read_db_config()

    try:
        print 'Connecting to database: {0}...'.format(db_config['database'])
        conn = MySQLConnection(**db_config)

        if conn.is_connected():
            print 'Connection established.'
        else:
            print 'Connection failed.'

    except Error as e:
        print e.message

    finally:
        conn.close()
        print 'Connection closed.'


def connect2():

    db_config = read_db_config()

    try:
        print 'Connecting to database: {0}...'.format(db_config['database'])
        conn = MySQLConnection(**db_config)

        if conn.is_connected():
            print 'Connection established.'
            return conn
        else:
            print 'Connection failed.'

    except Error as e:
        print e.message



def query_with_fetchone(query):

    conn = connect2()
    cursor = conn.cursor()
    cursor.execute(query)

    # Fetchone() method to fetch the next row in the result set
    row = cursor.fetchone()

    while row is not None:
        print(row)
        row = cursor.fetchone()

    cursor.close()
    conn.close()


def query_with_fetchall(query):

    conn = connect2()
    cursor = conn.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()

    print 'Total Row(s) is {0}'.format(cursor.rowcount)
    for row in rows:
        print(row)

    cursor.close()
    conn.close()


def iter_row(cursor, size):
    while True:
        rows = cursor.fetchmany(size)
        if not rows:
            break
        for row in rows:
            yield row


def query_with_fetchmany(query, size=10):

    conn = connect2()
    cursor = conn.cursor()
    cursor.execute(query)

    for row in iter_row(cursor, size):
        print(row)

    cursor.close()
    conn.close()
