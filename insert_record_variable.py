import mysql.connector as mydbconnection
from mysql.connector import Error

def connect(id, name, price, purchase_date):
    conn = None

    try:

        conn = mydbconnection.connect(
            database='usersdb',
            user='root',
            password='Password'
        )
        print('☑️ Connection to SQL DB Successful')

        cursor = conn.cursor()

        mySql_insert_query = """INSERT INTO Laptop (Id, Name, Price, Purchase_date)VALUES (%s, %s, %s, %s) """

        record = (id, name, price, purchase_date) # adding values to tuple for inserting into query

        cursor.execute(mySql_insert_query, record)
        conn.commit()
        print('✔️ Records successfully added to laptop table')

    except Error as e:
        print(f'❎ Error: {e}')


    finally:
        if conn is not None and conn.is_connected():
            conn.close()
            print('🔚 SQL Connection Closed')


if __name__ == '__main__':
    connect(23, 'Macbook Pro', 2000, '2026-01-01')