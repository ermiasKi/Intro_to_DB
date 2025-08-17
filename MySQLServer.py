import mysql.connector


try:
    mydb = mysql.connector.connect(
        host='localhost',
        user='root',
        password='******'
    )

    cursor = mydb.cursor()

    cursor.execute('CREATE DATABASE IF NOT EXISTS alx_book_store;')

    cursor.commit()
    cursor.close()
    mydb.close()

    print("Database 'alx_book_store' created successfully!")
except:
    print("Database 'alx_book_store' has already createds!")