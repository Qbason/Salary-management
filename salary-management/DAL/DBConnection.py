#import connectora
import mysql.connector

#utworzenie obiektu łączącego się do bazy wedle ustawien
my_db = mysql.connector.connect(
                host="192.168.1.10",
                user="user",
                password="zaq1@WSX",
                database="salarymanagement",
                port = "3306"
            )

