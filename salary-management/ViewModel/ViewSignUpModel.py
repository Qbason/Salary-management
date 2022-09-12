from DAL.Entity.User import User
from DAL.Entity.Employee import Employee
from DAL.Entity.Contract import Contract
from DAL.Repository.RepositoryUser import RepositoryUser
from DAL.Repository.RepositoryEmployee import RepositoryEmployee
from DAL.Repository.RepositoryContract import RepositoryContract
import re
from datetime import datetime


class ViewSignUpModel():
    def __init__(self,get_model):
        self.model = get_model
        self.users = get_model.dict_of_tables["users"]

        #make sure that every field is validated correctly
        self.validation_field={
            "firstname":False,
            "lastname":False,
            "login":False,
            "passwd":False,
            "email":False,
            "hourlyrate":False,
            "companyname":False,
            "startingdate":False,
            "expirationdate":False

        }
        #the list, which is responsible for holding warning, as a validation of 
        self.validation_result=[]


    # function which delete the warning from list
    def delete_from_validation_result(self,text):
        if self.validation_result.count(text) >0:
            self.validation_result.remove(text)
            return True
        else:
            return False

    # create string from list validation result
    def validation_result_to_string(self):
        return "\n".join(self.validation_result)

    # add warning to list validation result, if it dooesnt exist
    def add_to_validation_result(self,warning):
        if warning not in self.validation_result:
            self.validation_result.append(warning)


    def check_if_such_user_already_no_exists(self,get_login):
        user=RepositoryUser().FindUser(get_login,"",password_too=False)
        if user==False:
            return True
        return False
    
       



    #checking if text is coninst of letters
    def check_if_text_is_consist_of_letters(self,text):
        return text.isalpha()

    #checking if the length is not too long and too short
    def check_if_length_is_correct(self,text):
        
        if len(text)==0 or len(text)>50:
            return False
        return True

    #finding space in the text
    def check_if_has_no_space(self,text):
        return not text.find(" ")!=-1

    
    def check_if_it_is_date_format(self,get_string):
        #checking if the user has written the date properly
        try:
            #try to parse #format day-month-year
            d = datetime.strptime(get_string, '%d.%m.%Y').date()
            get_string = d
            return True
        except:
            return False

    def check_if_it_contains_only_letters(self,text):
        return text.isalpha()

    def check_email_regexp(self,get_email):
        regex_email = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

        if re.fullmatch(regex_email,get_email):
            return True
        else:
            return False   

    def check_if_it_is_a_number(self,get_text):
        try:
            get_text = float(get_text)
            return True
        except:
            return False



    def tests_validation(self,get_text,warnings,tests,name_key_of_validation_field):
        "get text to validate, warnings, validations functions, name of the validation field"


        if len(tests) != len(warnings):
            return False

        #assumed that test is passed well
        r = True 

        #take number of numbers of tests
        for num in range(0,len(tests)):
            #if test is not passed..
            if not tests[num](get_text):
                #add warning which is bonded with test
                self.add_to_validation_result(warnings[num])
                r = False
                #break
            else:
                self.delete_from_validation_result(warnings[num])
        
        #if the error appeared then validation didnt pass
        if r==False:
            self.validation_field[name_key_of_validation_field] = False
        else:
            self.validation_field[name_key_of_validation_field] = True

        return True



    
    #checking if the user already exists
    def check_entry_login(self,get_login):
     
        #set warning
        warning = ["Nieprawidłowo podany login", "Login zawiera spacje","Taki user juz istnieje"]
        #set tests
        tests = [self.check_if_length_is_correct,self.check_if_has_no_space,self.check_if_such_user_already_no_exists]
        
        #do test
        if self.tests_validation(get_login,warning,tests,"login"):

            return self.validation_result_to_string()
        
        else:
            raise("Tests and warning doesn't equal")

    #checking if the  firstname is correct
    def check_entry_firstname(self,get_firstname):
        
        #set warning
        warning = ["Nieprawidłowa długośc imienia", "Imie zawiera spacje","Imie zawiera nieprawidłowe znaki"]
        #set tests
        tests = [self.check_if_length_is_correct,self.check_if_has_no_space,self.check_if_it_contains_only_letters]

        if self.tests_validation(get_firstname,warning,tests,"firstname"):
            return self.validation_result_to_string()
        else:
            raise("Tests and warning doesn't equal")
        

    #checking if the lastname is correct

    def check_entry_lastname(self,get_lastname):

        #set warning
        warning = ["Nieprawidłowa długość nazwiska", "Nazwisko zawiera spacje","Nazwisko zawiera nieprawidłowe znaki"]
        #set tests
        tests = [self.check_if_length_is_correct,self.check_if_has_no_space,self.check_if_it_contains_only_letters]

        if self.tests_validation(get_lastname,warning,tests,"lastname"):
            return self.validation_result_to_string()
        else:
            raise("Tests and warning doesn't equal")

    #do simple check entry password based on the method tests_validation
    def check_entry_passwd(self,get_passwd):
        warning = ["Nieprawidłwa długość hasła","Hasło zawiera spacje"]
        tests = [self.check_if_length_is_correct,self.check_if_has_no_space]

        if self.tests_validation(get_passwd,warning,tests,"passwd"):
            return self.validation_result_to_string()
        else:
            raise("Tests and warning doesn't equal")


    def check_entry_email(self,get_email):
        
        warning  =  ["Nieprawidłowy email"]
        tests = [self.check_email_regexp]

        if self.tests_validation(get_email,warning,tests,"email"):
            return self.validation_result_to_string()
        else:
            raise("Tests and warning doesn't equal")
        

    def check_entry_companyname(self,get_comapnyname):

        warning = ["Nazwa firmy nie moze byc pusta"]
        tests = [self.check_if_length_is_correct]

        if self.tests_validation(get_comapnyname,warning,tests,"companyname"):
            return self.validation_result_to_string()
        else:
            raise("Tests and warning doesn't equal")
        

    def check_entry_hourlyrate(self,get_hourlyrate):

        warning = ["Stawka nie moze być pusta!","Prawidłowy format: $.$"]
        #functions, which are used to do tests
        tests = [self.check_if_length_is_correct,self.check_if_it_is_a_number]
        
        if self.tests_validation(get_hourlyrate,warning,tests,"hourlyrate"):
            return self.validation_result_to_string()
        else:
            raise("Tests and warning doesn't equal")


    def check_entry_startingdate(self,get_startingdate):
        warning = ["Prawidłowy format daty rozpoczęcia to  dd.mm.yy"]
        tests = [self.check_if_it_is_date_format]

        if self.tests_validation(get_startingdate,warning,tests,"startingdate"):
            return self.validation_result_to_string()
        else:
            raise("Tests and warning doesn't equal")

    def check_entry_expirationdate(self,get_expirationdate):
        warning = ["Prawidłowy format daty zakończenia to  dd.mm.yy"]
        tests = [self.check_if_it_is_date_format]

        if self.tests_validation(get_expirationdate,warning,tests,"expirationdate"):
            return self.validation_result_to_string()
        else:
            raise("Tests and warning doesn't equal")       



    #walidacja i dodanie nowej osoby do bazy danych
    def add_person(self,**kwargs
    ):
        dict_person = kwargs
        validation_field = self.validation_field.copy()

        for key, value in kwargs.items():
            #print("{0} = {1}".format(key,value))
            #change expirationdate if someone chose Umowa o prace na czas nieokreślony
            #the assumption is that the same date of starting and expiration date means that 
            #user is on Umowa o prace na czas nieokreślony
            if key=="type" and value == "Umowa o prace na czas nieokreślony":
                
                validation_field["expirationdate"]=True
                dict_person["expirationdate"] = dict_person["startingdate"]

            elif key=="type" and value == "Umowa zlecenie":
                #changing data dayjob 
                self.validation_field["dayjob"] = True
                dict_person["dayjob"] ="-"

        #print(validation_field.values())

        #chceking if the user filled all fields properly
        if False in validation_field.values():
            return "Niepoprawnie uzupełnione pola"
        
        #correcting letter 
        dict_person["login"]=dict_person["login"].lower()
        dict_person["firstname"]=dict_person["firstname"].lower().capitalize()
        dict_person["lastname"]=dict_person["lastname"].lower().capitalize()
        dict_person["email"]=dict_person["email"].lower()



        #creating  objects 
        new_user = User()
        new_employee = Employee()
        new_contract = Contract()

        #finding the feature for example:login,firstname in keys() of object dict
        #then save the feature to specific object
        for feature in dict_person.keys():
            if feature in new_user.dict_user.keys():
                new_user.dict_user[feature] = dict_person[feature]

            elif feature in new_employee.dict_employee.keys():
                new_employee.dict_employee[feature] = dict_person[feature]

            elif feature in new_contract.dict_contract.keys():
                new_contract.dict_contract[feature] = dict_person[feature]

        try:
            #adding to database
            #add user to database and get id_user
            id_user = RepositoryUser().add_newuser(new_user)
            if id_user == -1:
                raise "Błąd z komunikacją"
            new_user.dict_user["id_user"] = id_user
            new_employee.dict_employee["id_employee"]=id_user
            new_contract.dict_contract["id_contract"]=id_user
            #add new employee based on new id_user
            RepositoryEmployee().add_new_employee(new_employee)
            #add new contract based on  new id_user
            RepositoryContract().add_new_contract(new_contract)

        except:
            return "Błąd połączenia z bazą danych"

        finally:
            try:
                #adding new user, new employee and new contract to actual model of objects
                self.model.dict_of_tables["users"].append(new_user)
                self.model.dict_of_tables["employees"].append(new_employee)
                self.model.dict_of_tables["contracts"].append(new_contract)
                return "Pomyślnie zarejestrowano"
            except Exception as e:
                return "Błąd przy rejestracji"
           
                
        
       

        
