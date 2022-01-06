from DAL.Repository.BaseRepository import BaseRepository
from DAL.Entity.Employee import Employee
from DAL.DBConnection import my_db
class RepositoryEmployee(BaseRepository):


    ALL_EMPLOYEES = "SELECT *  FROM `employee` where id_employee={}"
    ADD_EMPLOYEE = "INSERT INTO `employee`(`id_employee`,`firstname`,`lastname`) VALUES "

    def TakesAll(self,id_employee):
        try:
            return self.get_all_rows(self.ALL_EMPLOYEES.format(id_employee),Employee)
        except Exception as e:
            print("Fatal error",e)

    def add_new_employee(self,employee):
        wynik = False
        try:
            #sprawdzenie czy polaczono z baza danych
            if my_db.is_connected():
                #extracting data
                id_employee = employee.dict_employee["id_employee"] 
                firstname = employee.dict_employee["firstname"]
                lastname = employee.dict_employee["lastname"]
                mycursor = my_db.cursor()
                #create query
                query = self.ADD_EMPLOYEE + "('{0}','{1}','{2}')".format(
                    id_employee,
                    firstname,
                    lastname
                
                    )
                print(query)
                wynik = mycursor.execute(query)
                my_db.commit()

        except Exception as e:
            print("Error while connecting to MySQL",e)
        finally:
            if my_db.is_connected():
                mycursor.close()
                #my_db.close()
                
                return wynik 