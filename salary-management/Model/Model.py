from DAL.Repository.RepositoryEmployee import  RepositoryEmployee
from DAL.Repository.RepositoryContract import  RepositoryContract
from DAL.Repository.RepositorySchedule import  RepositorySchedule
from DAL.Repository.RepositoryUser import  RepositoryUser



class Model():

    def __init__(self):
        self.dict_of_tables = {
            "employees" : [],#RepositoryEmployee().TakesAll(),
            "contracts" : [],#RepositoryContract().TakesAll(),
            "schedules" : [],#RepositorySchedule().TakesAll(),
            "users" : []#RepositoryUser().TakesAll()
        }       
    
  