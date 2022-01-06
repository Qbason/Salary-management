from tkinter import *
from View.ViewSignUp import ViewSignUp
from View.ViewTabs import ViewTabs



class ViewLogging():

    def __init__(self,main_view_model):
        
        #przygotowanie zmiennych pod obiekty widokow
        self.mainviewmodel = main_view_model
        self.viewloggingmodel = main_view_model.viewloggingmodel
        self.rootofsignup = object
        self.rootofnotebook = object

        #konfiguracja głównego okna
        self.rootofviewlogging = Tk()
        self.rootofviewlogging.resizable(False,False)
        self.rootofviewlogging.title("Salary-Managment")

        #label pod username
        self.l_username = Label(self.rootofviewlogging,width=30,text="Login: ")
        self.l_username.grid(row=0,column=3,columnspan=6,pady=10)
        
        #entry pod username
        self.e_username  = Entry(self.rootofviewlogging, width=30)
        self.e_username.grid(row=1,column=3,columnspan=6)

        #label pod password
        self.l_password = Label(self.rootofviewlogging,width=30,text="Hasło: ")
        self.l_password.grid(row=2,column=3,columnspan=6,pady=10)

        #entry pod password
        self.e_password  = Entry(self.rootofviewlogging, width=30, show="*")
        self.e_password.grid(row=3,column=3,columnspan=6,pady=(0,10))

        #lable pod wypisanie wyniku
        self.l_result = Label(self.rootofviewlogging,width=30,text="")
        self.l_result.grid(row=4,column=3,columnspan=6)

        #button pod zaloguj sie
        self.b_login = Button(self.rootofviewlogging,width=30,text="Zaloguj sie",
        command=self.check_user)
        self.b_login.grid(row=5,column=0,columnspan=5,padx=15,pady=30)

        #button pod zarejestruj sie
        self.b_signup = Button(self.rootofviewlogging,width=30,text="Zarejestruj sie",command=self.sign_up)
        self.b_signup.grid(row=5,column=7,columnspan=5,padx=15)


        self.rootofviewlogging.mainloop()

    def sign_up(self):
        self.rootofsignup = ViewSignUp(self.mainviewmodel)
        

    def check_user(self):
        self.e_username.insert(0,"jakukos392")
        self.e_password.insert(0,"123123123")
        
       # self.e_username.insert(0,"maro")
       # self.e_password.insert(0,"123123123")
        
        user = self.viewloggingmodel.check_if_is_in_database(self.e_username.get(),self.e_password.get())
        if  user!= None:
            self.l_result["text"] = "Zalogowano"
            self.rootofviewlogging.destroy()
            self.rootofnotebook = ViewTabs(self.mainviewmodel,user)
        else:
            self.l_result["text"] = "Nieprawidłowe dane"
            

    

    



    