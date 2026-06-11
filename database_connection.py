import pymysql
from pymysql.constants.FIELD_TYPE import VARCHAR

from my_string import name

con=pymysql.connect(
    host="localhost",
    user="root",
    passwd="Root",
    db="test",
    charset="utf8",
    cursorclass=pymysql.cursors.DictCursor
)

# cursor is to execute in our mysql
try:
    with con.cursor() as cursor:

        create_query="""CREATE TABLE IF NOT EXISTS employees(
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100),
            department VARCHAR(100)
        );"""
        cursor.execute(create_query)

        insert_query="""INSERT INTO employees(name, department) VALUES (%s, %s);"""
        values=[("John","IT"),("Alice","CSC")]
        # executing more than one values,that's why giving executemany
        cursor.executemany(insert_query, values)
        con.commit()

        select_query="""SELECT * FROM employees;"""
        cursor.execute(select_query)
        # to read(fetch)
        result=cursor.fetchall()


        with open("emplyees_output.txt","w") as f:
            for row in result:
                f.write(f"{row}\n")
finally:
    con.close()
