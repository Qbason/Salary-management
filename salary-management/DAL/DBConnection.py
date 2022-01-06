#import connectora
import mysql.connector

#utworzenie obiektu łączącego się do bazy wedle ustawien
my_db = mysql.connector.connect(
                host="78.157.187.16",
                user="user",
                password="123123123",
                database="salarymanagement",
                port = "3307"
            )

