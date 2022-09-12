from DAL.Entity.BaseEntity import BaseEntity

from datetime import date



class Contract(BaseEntity):
    def __init__(self):
        self.dict_contract = {
        "id_contract": int(),
        "type":str(),
        "startingdate": date.today(),
        "expirationdate": date.today(),
        "companyname": str(),
        "dayjob":str(),
        "hourlyrate":float()
        }

    def return_dict(self):
        return self.dict_contract

    def __str__(self):
        return f'''
                ID: {self.dict_contract["id_contract"]} 
                Type: {self.dict_contract["type"]} 
                Starting date: {self.dict_contract["startingdate"]} 
                Expiration rate: {self.dict_contract["expirationdate"]} 
                Companyname: {self.dict_contract["companyname"]}
                Day job: {self.dict_contract["dayjob"]} 
                Hourly rate: {self.dict_contract["hourlyrate"]}  
                '''
