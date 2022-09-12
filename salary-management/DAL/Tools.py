from datetime import date

#narzedzia pomagajace ulatwic prace

#metoda zwracajaca sparsowana zmienna wedlug typu podanej zmiennej(branej z obiektu, obiekt dofiniuje typ podstawowy)
def return_parsed_variable(type_variable, variable):

    try:
        if(isinstance(type_variable,int)):
            return int(variable)
        elif(isinstance(type_variable,float)):
            return float(variable)
        elif(isinstance(type_variable,str)):
            return str(variable)
        elif(isinstance(type_variable,date)):
            return date.strftime(variable,"%Y-%m-%d")
        else:
            print("Not known type")
    except:
        print("Empty column in database")
        #raise("Empty column")

