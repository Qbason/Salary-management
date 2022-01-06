from DAL  import Tools

class BaseEntity():
#funkcja przypisujaca dane do zmiennych klas

    def assign_from_database(self,row_from_database,dict_columns_names):
        #ustalenie nazwy kolumn, które są przez nas wymagane
        #nazwy pobierane są z słownika utworzonego przy tworzeniu obiektu
        column_names_from_object = self.return_dict()
    
        #petla na potrzeby przypisania zmiennych
        for column_name_object in column_names_from_object:
            #jezeli nazwa kolumny istnieje w nazwach kolumn zaimportowanych
            if column_name_object in dict_columns_names.keys():
                #przypisz do slownika nowy klucz i przypisz mu wartosc
                column_names_from_object[column_name_object] = Tools.return_parsed_variable(column_names_from_object[column_name_object],row_from_database[dict_columns_names[column_name_object]]) #korzystamy ze slownika, aby zwrocil nam numer odpowiadajacej kolumny
            else:
                #jezeli columna nie zostala znaleziona zwroc False
                return False


        return True