import mysql.connector as mydbconnection
from mysql.connector import Error


def connect():
    conn = None

    try:
        conn = mydbconnection.connect(database='classicmodels', user='root', password='Password')

        if conn.is_connected():
            print('✅ Connected to MySQL DB')
    
    except Error as e:
        print(f'❌ Error: {e}')

    finally: # runs whether operation failed or not (Always runs)
        # Close our connection
        if conn is not None and conn.is_connected():
            conn.close()
            print('🛑 DB Connection Closed')


if __name__ == '__main__':
    connect()