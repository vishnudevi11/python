import mysql


def connect_to_mysql():
    con=mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="get_decrypted_password()",
        db="test",
    )
    print("Connected to mysql successfully")
    con.close()

if __name__ == "__main__":
    connect_to_mysql()