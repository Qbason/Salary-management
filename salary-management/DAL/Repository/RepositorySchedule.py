from DAL.Repository.BaseRepository import BaseRepository
from DAL.Entity.Schedule import Schedule
from DAL.DBConnection import my_db

class RepositorySchedule(BaseRepository):

   
    #queries
    ALL_SCHEDULES = "SELECT *  FROM `schedule` where id_employee={}"
    ADD_SCHEDULE = "INSERT INTO `schedule`(`date`,`hours`,`id_employee`) VALUES "
    EDIT_SCHEDULE = "UPDATE `schedule` set hours='{}' where id_schedule = {}"
    DROP_SCHEDULE = "delete from `schedule` where id_schedule={}"

    def TakesAll(self,id_employee):
        try:
            return self.get_all_rows(self.ALL_SCHEDULES.format(id_employee),Schedule)
        except Exception as e:
            print("Fatal error",e)

    def add_new_schedule(self,schedule):
        wynik = False
        try:
            #sprawdzenie czy polaczono z baza danych
            if my_db.is_connected():
                #extracting data 
                date = schedule.dict_schedule["date"]
                hours = schedule.dict_schedule["hours"]
                #print(hours)
                id_user = schedule.dict_schedule["id_employee"]
                
                mycursor = my_db.cursor()
                #create query
                query = self.ADD_SCHEDULE + "('{0}','{1}','{2}')".format(
                    date,
                    hours,
                    id_user

                
                    )
                #print(query)
                mycursor.execute(query)
                wynik = mycursor.lastrowid 
                my_db.commit()

        except Exception as e:
            print("Error while connecting to MySQL",e)
        finally:
            if my_db.is_connected():
                mycursor.close()
                #my_db.close()
                
                return wynik 

    def edit_schedule(self,id_schedule,hour):

        wynik = False
        try:
            #sprawdzenie czy polaczono z baza danych
            if my_db.is_connected():
                #create cursor
                mycursor = my_db.cursor()
                #create query
                query = self.EDIT_SCHEDULE.format(hour,id_schedule)
                #print(query)
                wynik = mycursor.execute(query)
                my_db.commit()

        except Exception as e:
            print("Error while connecting to MySQL",e)
        finally:
            if my_db.is_connected():
                mycursor.close()
                #my_db.close()
                return wynik 



    def delete_schedule(self,id_schedule):
    
        wynik = False
        try:
            #sprawdzenie czy polaczono z baza danych
            if my_db.is_connected():
                #create cursor
                mycursor = my_db.cursor()
                #create query
                query = self.DROP_SCHEDULE.format(id_schedule)
                #print(query)
                wynik = mycursor.execute(query)
                my_db.commit()

        except Exception as e:
            print("Error while connecting to MySQL",e)
        finally:
            if my_db.is_connected():
                mycursor.close()
                #my_db.close()
                return wynik 