#from DAL.Entity.employee import employee
#from DAL import DBConnection 
from Model.Model import Model


nowy_model = Model()


#print(nowy_model.dict_of_table.keys())

for one_element in nowy_model.dict_of_tables:
        for one_object in nowy_model.dict_of_tables[one_element]:
            print(one_object)

