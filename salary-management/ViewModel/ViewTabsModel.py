from DAL.Entity.Schedule import Schedule
from DAL.Entity.User import User
from DAL.Entity.Employee import Employee
from DAL.Entity.Contract import Contract
from DAL.Repository.RepositorySchedule import RepositorySchedule
from DAL.Repository.RepositoryUser import RepositoryUser
from DAL.Repository.RepositoryEmployee import RepositoryEmployee
from DAL.Repository.RepositoryContract import RepositoryContract

from datetime import datetime,date
import numpy as np
from dateutil.relativedelta import relativedelta

#testing
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg



class ViewTabsModel():
    def __init__(self,get_model):
        #creating instance of the model
        self.model = get_model
        self.users = get_model.dict_of_tables["users"]
        self.employees = get_model.dict_of_tables["employees"]
        self.schedules = get_model.dict_of_tables["schedules"]
        self.contracts = get_model.dict_of_tables["contracts"]

        #variables, which are used in the frame2
        self.sort_type = None
        self.sort_order = False
        self.filter_hours = ""
        self.filter_month = ""
        self.filter_year = ""
        self.sum_hours_after_filter = 0

    #return firstname based od user id
    def get_firstname(self,user):
        #find employee by id_user
        #debugging#print(user,"in the get_firstname")
        
        for employee in self.employees:
            #debugging#print(employee)
            if user.dict_user["id_user"] == employee.dict_employee["id_employee"]:
                return employee.dict_employee["firstname"]
        return "-"
    
    #functions which extracts full date, year, month, day from today
    def get_today(self):
        return date.today().strftime("%d.%m.%Y")

    def get_today_year(self):
        return int(date.today().strftime("%Y"))

    def get_today_month(self):
        return int(date.today().strftime("%m"))

    def get_today_day(self):
        return int(date.today().strftime("%d"))

    #getting hours from schedule based on user and chose day
    def get_hours_from_schedule(self,user,chose_day):
        chose_day = datetime.strptime(chose_day,'%d.%m.%Y').strftime("%Y-%m-%d")
        for schedule in self.schedules:
            #print(schedule)
            #if schedule.dict_schedule["id_employee"] == user.dict_user["id_user"]:
                #print(schedule.dict_schedule["date"], chose_day,"----------")
                if schedule.dict_schedule["date"] == chose_day:
                    return schedule.dict_schedule["hours"]
        return "-"
    #setting 

    def is_it_a_number(self,number):
        "true if it is a number (float)"
        try:
            number = float(number)
            return True
        except:
            return False



    def set_hour_to_schedule(self,user,chose_day,hour):
        #changing format of date(because of database)
        chose_day = datetime.strptime(chose_day,'%d.%m.%Y').strftime("%Y-%m-%d")
        try:
            #checking if our hours is no equal l4 or d which are shift and sick leave
            if self.is_it_a_number(hour):
                hour = float(hour)
            elif "l4" != hour.lower() and "d" != hour.lower() and "-"!= hour:
                raise ValueError
            else:
                hour = hour.lower()
            #changing letter to low
            
            #finding schedule by id_user
            for schedule in self.schedules:
                #print(schedule)
               # if schedule.dict_schedule["id_employee"] == user.dict_user["id_user"]:
                    #print(schedule.dict_schedule["date"], chose_day,"----------")
                    #checking if date is equal to chose day in calendar
                    if schedule.dict_schedule["date"] == chose_day:
                        #add to database
                        if hour=="-":
                            RepositorySchedule().delete_schedule(
                                schedule.dict_schedule["id_schedule"]
                            )
                            self.schedules.remove(schedule)

                        else:
                            RepositorySchedule().edit_schedule(
                                schedule.dict_schedule["id_schedule"],
                                hour
                            )
                            #add to actual model
                            schedule.dict_schedule["hours"] = hour
                        #print("Zaaktualizono!")
                        return
            if hour=="-":
                return
            #if method above doesn't work then we have to create a new record
            #create obj and setting values
            new_schedule = Schedule()
            new_schedule.dict_schedule["date"] = chose_day
            new_schedule.dict_schedule["hours"] = hour
            new_schedule.dict_schedule["id_employee"] = user.dict_user["id_user"]
            #add to database
            last_id = RepositorySchedule().add_new_schedule(new_schedule)
            if last_id!=False:
                new_schedule.dict_schedule["id_schedule"] = last_id
                self.schedules.append(new_schedule)
            #add to actual model
            #print(last_id)
            #print(new_schedule.show())
          

            #print("Dodano nowy wpis")
        except ValueError:
            print("Parsing to float didn't work")


    def find_months_and_year(self,user):
        """finding, when the employee works, in which years and months
            returning list, which elements has format YM Y-year M-month"""
        
        dict_year_month = []
        
        for schedule in self.schedules:
            #print(schedule)
            #finding schedule by id_user
            #if schedule.dict_schedule["id_employee"] == user.dict_user["id_user"]:
                year_month = (datetime.strptime(schedule.dict_schedule["date"],"%Y-%m-%d").strftime("%Y%m"))
                
                if year_month not in dict_year_month:
                    dict_year_month.append(year_month)
                
                
        return dict_year_month



    #do poprawy ma zliczać sume nadgodzin tylko w miesiącach kiedy pracował
    def get_the_overtime_all_time(self,user):
        overtime_sum = 0
        list_year_month = self.find_months_and_year(user)
        
        for year_month in list_year_month:
            sum_hours = self.get_sum_of_hours(
                user,
                year_month,
                full_date=False
            )
            sum_hours_should_work = self.get_hours_of_working(user,year_month,full_date=False)
            overtime_sum = overtime_sum + (sum_hours-sum_hours_should_work)
        
        
        return (overtime_sum)
        
    
    def get_sum_of_hours(self,user,chose_day,full_date=True):
        #getting sum of hours by chose month and year and finding by user
        
        sum = 0
        if full_date ==True:
            month_from_interface = datetime.strptime(chose_day,'%d.%m.%Y').strftime("%Y%m")
        else:
            month_from_interface = datetime.strptime(chose_day,'%Y%m').strftime("%Y%m")
        for schedule in self.schedules:
            #print(schedule)
            #finding schedule by id_user
           # if schedule.dict_schedule["id_employee"] == user.dict_user["id_user"]:
                #print(schedule)
                #checking if it is not d or l4
                if schedule.dict_schedule["hours"]!="d" and schedule.dict_schedule["hours"]!="l4":
                    month = datetime.strptime(schedule.dict_schedule["date"],"%Y-%m-%d").strftime("%Y%m")
                    #print(month, month_from_interface)
                    #if the month,year are the same then sum
                    if month == month_from_interface:
                        sum=float(schedule.dict_schedule["hours"])+sum
                        
        
        return sum


    def get_sum_of_shifts(self,user,chose_day,full_date=True):
        #getting sum of shifts, we can a "d"
        sum = 0
        if full_date==True:
            month_from_interface = datetime.strptime(chose_day,'%d.%m.%Y').strftime("%Y%m")
        else:
            month_from_interface = datetime.strptime(chose_day,'%Y%m').strftime("%Y%m")
        for schedule in self.schedules:
            #print(schedule)
            #finding schedules by id_user
            #if schedule.dict_schedule["id_employee"] == user.dict_user["id_user"]:
                #print(schedule)
                #checking if the shedule has a "d"
                if schedule.dict_schedule["hours"]=="d":
                    month = datetime.strptime(schedule.dict_schedule["date"],"%Y-%m-%d").strftime("%Y%m")
                    #print(month, month_from_interface)
                    #checking if the month and year are equal
                    if month == month_from_interface:
                        sum=sum+1
        return sum

    def get_sum_of_leave_sick(self,user,chose_day,full_date=True):
        #getting sum of leave sick in a year,month
        sum = 0
        #get only year and month from full date
        if full_date==True:
            month_from_interface = datetime.strptime(chose_day,'%d.%m.%Y').strftime("%Y%m")
        else:
            month_from_interface = datetime.strptime(chose_day,'%Y%m').strftime("%Y%m")
            
            
        for schedule in self.schedules:
        
            #fidning schedule for id_user
            #if schedule.dict_schedule["id_employee"] == user.dict_user["id_user"]:
               #checking if the hour is equal to l4
                if schedule.dict_schedule["hours"]=="l4":
                    #substract and get only year and month
                    month = datetime.strptime(schedule.dict_schedule["date"],"%Y-%m-%d").strftime("%Y%m")
                    #checking if the year and month are the same
                    if month == month_from_interface:
                        sum=sum+1
        return sum

    #return dayjob from contact based on id_user
    def get_dayjob(self,user):
        "return dayjob or ''"
        for contract in self.contracts:
            #if contract.dict_contract["id_contract"] == user.dict_user["id_user"]:
                dayjob = contract.dict_contract["dayjob"]
                #date_start = contract.dict_contract["startingdate"]
                return dayjob
        return ""
    
    
      #return hourlyrate from contact based on id_user
    def get_hourlrate(self,user):
        "return dayjob or ''"
        for contract in self.contracts:
            #if contract.dict_contract["id_contract"] == user.dict_user["id_user"]:
                hourlyrate = contract.dict_contract["hourlyrate"]
                return hourlyrate
        return ""

    #get hours multiple by hourlyrate based on id_user
    def value_of_earned_money(self,user,hours):
        for contract in self.contracts:
            #if contract.dict_contract["id_contract"] == user.dict_user["id_user"]:
                hourlyrate = contract.dict_contract["hourlyrate"]
                return float(hours)*float(hourlyrate)
        return -1

    #calucalting how many hours we have to work in specific month
    def get_hours_of_working(self,user,chose_day,full_date=True):
        "user(object), chose_day from schedule"
        #zrobic porownanie dat, tak, że tylko jeżeli 
        #data jest nowsza od daty rozpoczecia umowy to wtedy liczmy ile ma robic
        dayjob = str()

        #print(user,"in the get_hours_of_working")

        for contract in self.contracts:
            #if contract.dict_contract["id_contract"] == user.dict_user["id_user"]:
                dayjob = contract.dict_contract["dayjob"]
                #date_start = contract.dict_contract["startingdate"]
                if dayjob == "-":
                    return 0
                break


        if full_date:
            #create obj type dateime
            date_full = datetime.strptime(chose_day,'%d.%m.%Y')
           
        else:
            date_full = datetime.strptime(chose_day,'%Y%m')
           
            
        #get year from obj
        year = date_full.year
        #get month from obj
        month = date_full.month
        #count the last day of month
       
       
       #days when have holidays
        holidayss = [
            "2021-01-01",
            "2021-01-06",
            "2021-04-05",
            "2021-04-05",
            "2021-05-01",
            "2021-05-03",
            "2021-06-03",
            "2021-08-15",
            "2021-11-01",
            "2021-11-11",
            "2021-12-25",
            "2021-12-26"

        ]
        #changing holidays year depending on user decision
        if year!=2021:
            for i in range(0,len(holidayss)):
                holidayss[i].replace("2021",str(year),1)

        #If the holidays is in the saturday, then we have one day more free 
        count_days = 0
        
        for holiday in holidayss:
            holiday_date = datetime.strptime(holiday,"%Y-%m-%d")
            if holiday_date.month == month:
                if holiday_date.isoweekday() == 6:
                    count_days = count_days - 1
                    #print("Uznano, że dzień",holiday_date,"to swieto wypadajace w sobote")

        #create starting date 
        start_date = date(year,month,1)
        #creating end date
        end_date = start_date+relativedelta(months=1)
        #count days  between 
        
        count_days = count_days + np.busday_count(start_date,end_date,holidays=holidayss)

        
        hours = RepositoryContract().tab_of_dayjob[dayjob](count_days) *  8

        return hours


###frame 2 


    def get_schedules(self,user,numbers,numbers_of_rows):
        schedules = []
        self.sum_hours_after_filter = 0
        for schedule in self.schedules:
            #if schedule.dict_schedule["id_employee"] == user.dict_user["id_user"]:
                r=True
                if self.filter_hours!="":
                    if schedule.dict_schedule["hours"].find(self.filter_hours)==-1:
                        ##NEED TO CHANGE !!!
                        r=False
                if self.filter_month!="":
                    if schedule.dict_schedule["date"].split("-")[1].find(self.filter_month)==-1:
                        ##NEED TO CHANGE !!!
                        r=False
                if self.filter_year!="":
                    #print(schedule.dict_schedule["date"].split("-")[0])
                    if schedule.dict_schedule["date"].split("-")[0].find(self.filter_year)==-1:
                        ##NEED TO CHANGE !!!
                        r=False

                if r:
                    schedules.append(schedule)
                    if self.is_it_a_number(schedule.dict_schedule["hours"]):
                        self.sum_hours_after_filter = float(schedule.dict_schedule["hours"])+self.sum_hours_after_filter
            
     
            

        if self.sort_type=="hours":
            schedules.sort(key=lambda x:str(x.dict_schedule["hours"]))
        elif self.sort_type=="year":
            schedules.sort(
                key=lambda x:x.dict_schedule["date"].split("-")[0]
                )
        elif self.sort_type=="month":
            schedules.sort(
                key=lambda x:x.dict_schedule["date"].split("-")[1]
                )

        if self.sort_order == True:
            schedules.reverse()

        return schedules[(numbers-1)*numbers_of_rows:numbers*numbers_of_rows]

    def change_sort_type_value(self,typee):
        self.sort_type = typee
        #print(typee)

    def change_sort_order_value(self,order):
        self.sort_order = order
        #print(order)

    def change_filter_hours_value(self,hours):
        self.filter_hours = hours
        #print(hours)

    def change_filter_month_value(self,month):
        self.filter_month = month
        #print(month)

    def change_filter_year_value(self,year):
        self.filter_year = year
        #print(year)

    def get_sum_hours_after_filter(self):
        return self.sum_hours_after_filter

#frame 3

    def calculate_salary(self,user,year,month,price_shift):
        base_dict = {}
        base_dict["hours"] = 0
        base_dict["shifts"] = 0
        base_dict["l4"] = 0
        
        if self.check_if_it_is_a_date(year,month):
            base_dict["hours"] = self.get_sum_of_hours(
                user,
                str(year)+str(month),
                full_date=False
                )
            
            base_dict["shifts"] = self.get_sum_of_shifts(
                user,
                str(year)+str(month),
                full_date=False
                )
            
            base_dict["l4"] = self.get_sum_of_leave_sick(
                user,
                str(year)+str(month),
                full_date=False
                )
            
        
        hourlyrate =  self.get_hourlrate(user)
      
        
        
        base_dict["overtime"] = 0
        
        if self.check_if_it_is_a_date(year,month):
            base_dict["overtime"] = base_dict["hours"]-self.get_hours_of_working(user,str(year)+str(month),full_date=False)
        
            
        
        if base_dict["overtime"]<0:
            base_dict["overtime"]=0
        
        base_dict["hours"] = base_dict["hours"] 
        
        base_dict["overtime_money"] = round(hourlyrate * base_dict["overtime"],3)
        
        base_dict["hours_money"] = round(self.value_of_earned_money(user,base_dict["hours"]) - base_dict["overtime_money"],3)
        
        if not self.is_it_a_number(price_shift):
            price_shift=0
        base_dict["shifts_money"] = round((base_dict["shifts"] * float(price_shift)),3)
        
        
        base_dict["l4_money"] = base_dict["l4"] * hourlyrate * 0.8
        
        base_dict["full"] = round((base_dict["hours_money"]) + (base_dict["shifts_money"])+(base_dict["l4_money"])+base_dict["overtime_money"],3)
        
        
        return base_dict
    
    
    def check_if_it_is_a_date(self,year,month):
        try:
            datee = date(int(year),int(month),1)
            return True
        except:
            return False