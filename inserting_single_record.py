import mysql.connector as mydbconnection
from mysql.connector import Error

def connect():
    conn = None

    try:

        conn = mydbconnection.connect(
            database='usersdb',
            user='root',
            password='Password'
        )
        print('Connected to SQL DB')



        cursor = conn.cursor()

        mySql_insert_query = """INSERT INTO Laptop (Id, Name, Price, Purchase_date) 
                           VALUES (15, 'Macbook Pro', 1785, '2026-04-14') """

        cursor.execute(mySql_insert_query)
        conn.commit()
        print(cursor.rowcount, "Record inserted successfully into laptop table")

        cursor.close()

    except Error as e:
        print(f'X Error: {e}')


    finally:
        if conn is not None and conn.is_connected():
            conn.close()
            print('DB Connection Closed')


if __name__ == '__main__':
    connect()