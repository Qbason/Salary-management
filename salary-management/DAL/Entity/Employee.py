from DAL.Entity.BaseEntity import BaseEntity

class Employee(BaseEntity):
    #stworzenie konstuktura inicjalizującego zmienne pod klase employee
    def __init__(self):

        self.dict_employee = {
        "id_employee": int(),
        "firstname": str(),
        "lastname": str()
        }

    def return_dict(self):
        return self.dict_employee

               
    def __str__(self):
        return f'''
                ID: {self.dict_employee["id_employee"]} 
                Firstname: {self.dict_employee["firstname"]} 
                Lastname: {self.dict_employee["lastname"]} 
                '''
                



        
   