from DAL.Entity.BaseEntity import BaseEntity
from datetime import date

class Schedule(BaseEntity):
    def __init__(self):
        self.dict_schedule = {
        "id_schedule": int(),
        "date": date.today(),
        "hours": str(),
        "id_employee": int()
        }

    def return_dict(self):
        return self.dict_schedule

    def __str__(self):
        return '{}\t{}'.format(
        "\t".join(self.dict_schedule["date"].split("-")),self.dict_schedule["hours"]
        )
    def show(self):
        return f'''
                ID: {self.dict_schedule["id_schedule"]} 
                Date: {self.dict_schedule["date"]} 
                Hours: {self.dict_schedule["hours"]} 
                Employee ID: {self.dict_schedule["id_employee"]} 
                '''