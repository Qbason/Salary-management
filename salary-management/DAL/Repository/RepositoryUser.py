from DAL.Repository.BaseRepository import BaseRepository
from DAL.Entity.User import User
from DAL.DBConnection import my_db

class RepositoryUser(BaseRepository):

  
    #queries
    ALL_USERS = "SELECT *  FROM `user`"
    ADD_USER = "INSERT INTO `user`(`login`,`email`,`passwd`) VALUES "
    FIND_USER = "SELECT *  FROM `user` where login=%s and passwd=%s"
    FIND_USER_BY_LOGIN = "SELECT *  FROM `user` where login=%s"

    def TakesAll(self):
        try:
            return self.get_all_rows(self.ALL_USERS,User)
        except Exception as e:
            print("Fatal error",e)

    
    def FindUser(self,login,password,password_too=True):
        try:
            Rows = []
            #sprawdzenie czy polaczono z baza danych
            if my_db.is_connected():
                #print("MYSQL connected")
                mycursor = my_db.cursor()
                #wykonaj zapytanie
                if password_too:
                    mycursor.execute(
                        self.FIND_USER,
                        (login,password,)
                        )
                else:
                    mycursor.execute(
                        self.FIND_USER_BY_LOGIN,
                        (login,)
                        )
                #pobierz nazwy kolumn z zapytania
                columns_names = [i[0] for i in mycursor.description]
                #zmiena z indexami i nazwami kolumn
                dict_columns_names = self.get_dict_of_column_names(columns_names)
                #pobranie zawartosci z wykonanego zapytania
                mysql_data_rows = mycursor.fetchall()
                
                if len(mysql_data_rows) > 0:
                    obj = User()
                    if obj.assign_from_database(mysql_data_rows[0],dict_columns_names) == False:
                        print("Nie ma takiej columny w bazie danych")
                    return obj
                else:
                    return False
                

        except Exception as e:
            print("Error while connecting to MySQL",e)
            return False
        finally:
            if my_db.is_connected():
                mycursor.close()



    def add_newuser(self,user):
        wynik = -1
        try:
            #sprawdzenie czy polaczono z baza danych
            if my_db.is_connected():
                login = user.dict_user["login"]
                email = user.dict_user["email"]
                passwd = user.dict_user["passwd"]
                mycursor = my_db.cursor()
                #wykonaj zapytanie
                query = self.ADD_USER + "('{0}','{1}','{2}')".format(login,email,passwd)
                print(query)
                mycursor.execute(query)
                my_db.commit()
                wynik = mycursor.lastrowid

        except Exception as e:
            raise("Error while connecting to MySQL",e)
        finally:
            if my_db.is_connected():
                mycursor.close()
                #my_db.close()
              
                return wynik 