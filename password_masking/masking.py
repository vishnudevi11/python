import mysql.connector

def connect_to_mysql():
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="Root",
        db="test",
        use_pure=True
    )

    print("Connected to MySQL")
    con.close()

if __name__ == "__main__":
    connect_to_mysql()