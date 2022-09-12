from DAL.DBConnection import my_db


class BaseRepository():

    #statyczna metoda do przerabiania tablicy z nazwami kolumn na slownik z nazwami kolumn zwracajacych index tablicy
    @staticmethod
    def get_dict_of_column_names(field_names):
        #przyklad
        # dict = { 0:"id_sth, 1:"name_sth"}
        result_dict = {}
        i = 0
        for key in field_names:
            result_dict[key] = i
            i += 1
        return result_dict

    def get_all_rows(self,query,class_entity):
        try:
            Rows = []
            #sprawdzenie czy polaczono z baza danych
            if my_db.is_connected():
                #print("MYSQL connected")
                mycursor = my_db.cursor()
                #wykonaj zapytanie
                mycursor.execute(query)
                #pobierz nazwy kolumn z zapytania
                columns_names = [i[0] for i in mycursor.description]
                #zmiena z indexami i nazwami kolumn
                dict_columns_names = self.get_dict_of_column_names(columns_names)
                #pobranie zawartosci z wykonanego zapytania
                mysql_data_rows = mycursor.fetchall()

                for row in mysql_data_rows:
                    obj = class_entity()
                    if obj.assign_from_database(row,dict_columns_names) == False:
                        print("Nie ma takiej columny w bazie danych")
                    Rows.append(obj)

        except Exception as e:
            print("Error while connecting to MySQL",e)
        finally:
            if my_db.is_connected():
                mycursor.close()
                #my_db.close()
                #print("MYSQL connection is closed")
                return Rows