from contextlib import closing

import pymysql as pymysql
import pymysql.cursors
from pymysql import OperationalError, MySQLError


def get_mysql(user: str, password: str, db: str, table: str) -> None:
    count = 0
    # Подключиться к базе данных.
    print("connect successful!!")
    try:
        with closing(pymysql.connect(host='127.0.0.1', user=user, password=password, db=db, charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor)) as conn:
            with conn.cursor() as cursor:  # SQL
                sql = "SELECT * FROM  {};".format(table)

                # Выполнить команду запроса (Execute Query).
                cursor.execute(sql)
                print(-1)
                # print("cursor.description: ", cursor.description)

                for row in cursor:
                    print(row)
                    count += 1
    finally:
        # Закрыть соединение (Close connection).
        # closing.close()
        print(count)


def add_mysql(user: str, password: str, db: str, table: str, id: int, name: str) -> None:
    connection = pymysql.connect(host='127.0.0.1',
                                 user=user,
                                 password=password,
                                 db=db,
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    print("connect successful!!")
    mycursor = connection.cursor()

    # sql = "INSERT INTO customers (name, address) VALUES (%s, %s,%s,%s)"
    try:
        sql = "INSERT INTO {} (id, name) VALUES (%s, %s)".format(table)
        val = (id, name)
        mycursor.execute(sql, val)
        print(mycursor.rowcount, "record inserted.")

        connection.commit()
        # Подключиться к базе данных
    except Exception as e:
        print('except')


def add_mysql_heap(user: str, password: str, db: str, table: str,
                   dict: tuple
                   ) -> None:  # ('root', 'password', 'sys', 'test', [(),(),()])
    try:
        connection = pymysql.connect(host='127.0.0.1',
                                     user=user,
                                     password=password,
                                     db=db,
                                     charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor)
        mycursor = connection.cursor()  # Подключиться к базе данных
    except OperationalError as e:
        print("Connection Error - >  %s", e)
    try:
        stmt = "INSERT INTO {} (id, name) VALUES (%s, %s)".format(table)
        mycursor.executemany(stmt, dict)
        connection.commit()
        print("#Successfull")
    except MySQLError as e:
        print("#FAILED - >  %s", e)
