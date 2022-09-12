from DAL.Repository.RepositoryEmployee import RepositoryEmployee
from DAL.Repository.RepositorySchedule import RepositorySchedule
from DAL.Repository.RepositoryUser import RepositoryUser
from DAL.Repository.RepositoryContract import RepositoryContract

class ViewLoggingModel():
    def __init__(self,get_model):
        self.model = get_model
    
    def add_to_list(self,elements,listname):
        for element in elements:
            listname.append(element)
    
    
    def check_if_is_in_database(self,login,password):
        
        user=RepositoryUser().FindUser(login,password)
        #if user exists
        if user is not False:
            id_user = user.dict_user["id_user"]
            #adding date to our application based on user id
            self.model.dict_of_tables["users"].append(user)
            self.add_to_list(RepositoryEmployee().TakesAll(id_user),self.model.dict_of_tables["employees"])
            self.add_to_list(RepositoryContract().TakesAll(id_user),self.model.dict_of_tables["contracts"])
            self.add_to_list(RepositorySchedule().TakesAll(id_user),self.model.dict_of_tables["schedules"])
            
            return user
  
        return None