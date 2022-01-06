from DAL.Entity.Contract import Contract
from DAL.Repository.BaseRepository import BaseRepository
from DAL.DBConnection import my_db

class RepositoryContract(BaseRepository):


    tab_of_dayjob = {
        "1/4": lambda x:x/4,
        "1/2": lambda x:x/2,
        "3/4": lambda x:x*3/4,
        "Pełny":lambda x:x
    }

    #queries
    ALL_CONTRACTS = "SELECT *  FROM `contract` where id_contract={}"
    ADD_CONTRACT = "INSERT INTO `contract`(`id_contract`,`type`,`startingdate`,`expirationdate`, `companyname`,`dayjob`,`hourlyrate`) VALUES "

    def TakesAll(self,id_user):
        try:
            return self.get_all_rows(self.ALL_CONTRACTS.format(id_user),Contract)
        except Exception as e:
            print("Fatal error",e)


    def add_new_contract(self,contract):
        wynik = False
        try:
            #sprawdzenie czy polaczono z baza danych
            if my_db.is_connected():
                #extracting data
                id_contract = contract.dict_contract["id_contract"] 
                type = contract.dict_contract["type"]
                startingdate = contract.dict_contract["startingdate"]
                expirationdate = contract.dict_contract["expirationdate"]
                companyname = contract.dict_contract["companyname"]
                dayjob = contract.dict_contract["dayjob"]
                hourlyrate = contract.dict_contract["hourlyrate"]
                mycursor = my_db.cursor()
                #create query
                query = self.ADD_CONTRACT + "('{0}','{1}','{2}','{3}','{4}','{5}','{6}')".format(
                    id_contract,
                    type,
                    startingdate,
                    expirationdate,
                    companyname,
                    dayjob,
                    hourlyrate
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


    