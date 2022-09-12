from tkinter import *
from tkinter import ttk

class ViewSignUp():

    def __init__(self,main_view_model):

        self.mainviewmodel = main_view_model
        self.viewsignupmodel = main_view_model.viewsignupmodel

        self.rootofviewsignup = Tk()
        
        self.rootofviewsignup.title("Rejestracja")
        self.rootofviewsignup.resizable(False,True)
        self.rootofviewsignup.minsize(height=600)
        self.rootofviewsignup.maxsize(height=900)
        

    
        

        ########################
        #label pod Imie
        self.l_firstname = Label(self.rootofviewsignup,text="Imię: "
        )
        self.l_firstname.grid(column = 0, row=0, pady=10,padx=10)
        #entry pod Imie
        self.e_firstname  = Entry(self.rootofviewsignup)
        self.e_firstname.grid(column = 1, row=0)
        #check if the firstname is correct
        self.e_firstname.bind("<KeyRelease>",self.check_entry_firstname)

        ########################

         #label pod Nazwisko
        self.l_lastname = Label(self.rootofviewsignup,text="Nazwisko: ")
        self.l_lastname.grid(column = 0, row=1, pady=10,padx=10)
        #entry pod Nazwisko
        self.e_lastname  = Entry(self.rootofviewsignup)
        self.e_lastname.grid(column = 1, row = 1)
        #check ifthe lastname is correct binding
        self.e_lastname.bind("<KeyRelease>",self.check_entry_lastname)

        ########################

        #label pod Login
        self.l_login = Label(self.rootofviewsignup,text="Login: ")
        self.l_login.grid(column = 0, row=2, pady=10,padx=10)
        #entry pod Login
        self.e_login  = Entry(self.rootofviewsignup)
        self.e_login.grid(column = 1, row=2)

        #sprawdzenie czy taki user juz istnieje
        self.e_login.bind("<KeyRelease>",self.check_entry_login)

        #########################

        #label pod Haslo
        self.l_passwd = Label(self.rootofviewsignup,text="Hasło: ")
        self.l_passwd.grid(column = 0, row=3, pady=10,padx=10)
        #entry pod Haslo
        self.e_passwd  = Entry(self.rootofviewsignup,show="*")
        self.e_passwd.grid(column = 1, row=3)

       #sprawdzenie czy haslo spelnia wymagania
        self.e_passwd.bind("<KeyRelease>",self.check_entry_passwd)
       

        #########################

        #label pod Email
        self.l_email = Label(self.rootofviewsignup,text="Email: ")
        self.l_email.grid(column = 0, row=4,pady=10,padx=10)
        #entry pod Email
        self.e_email  = Entry(self.rootofviewsignup)
        self.e_email.grid(column = 1, row=4)
        #checking if the email was written correctly
        self.e_email.bind("<KeyRelease>",self.check_entry_email)
        
        #########################

        #label pod Godzinowka
        self.l_hourlyrate = Label(self.rootofviewsignup,text="Stawka za godzine:")
        self.l_hourlyrate.grid(column = 0, row=5, pady=10,padx=10)
        #entry pod Godzinowka
        self.e_hourlyrate  = Entry(self.rootofviewsignup)
        self.e_hourlyrate.grid(column = 1, row=5)
         #checking if the hourlyrate was written correctly
        self.e_hourlyrate.bind("<KeyRelease>",self.check_entry_hourlyrate)
        #########################

        #label pod Nazwa firmy
        self.l_companyname = Label(self.rootofviewsignup,text="Nazwa firmy: ")
        self.l_companyname.grid(column = 0, row=6, pady=10,padx=10)
        #entry pod Nazwa firmy
        self.e_companyname  = Entry(self.rootofviewsignup)
        self.e_companyname.grid(column = 1, row=6)
        #checking if the companyname was written correctly
        self.e_companyname.bind("<KeyRelease>",self.check_entry_companyname)
        

        #########################

        #label pod Typ umowy
        self.l_type = Label(self.rootofviewsignup,text="Typ umowy: ")
        self.l_type.grid(column = 0, row=7, pady=10,padx=10)
        #combobox do wybrania typu umowy

        self.c_type = ttk.Combobox(self.rootofviewsignup, width=33, state="readonly",
                            values=[
                                    "Umowa o prace na czas okreslony", 
                                    "Umowa o prace na czas nieokreślony",
                                    "Umowa zlecenie"]
                                    )
    
        self.c_type.grid(column = 1, row=7,  padx=10)
        self.c_type.bind("<<ComboboxSelected>>",self.hide_show_dates)
        self.c_type.current(0)

        ########################

        #label pod etap
        self.l_dayjob = Label(self.rootofviewsignup,text="Etat: ")
        self.l_dayjob.grid(column = 0, row=8, pady=10,padx=10)

        #combobox do wybrania etatu
        self.c_dayjob = ttk.Combobox(self.rootofviewsignup, width=10, state="readonly",
                            values=[
                                    "1/4", 
                                    "1/2",
                                    "3/4",
                                    "Pełny"]
                                    )
    
        self.c_dayjob.grid(column = 1, row=8,  padx=10)
        self.c_dayjob.current(0)
        #########################

        #label pod czas rozpoczecia umowy
        self.l_startingdate = Label(self.rootofviewsignup,text="Czas rozpoczecia:")
        self.l_startingdate.grid(column = 0, row=9, pady=10,padx=10)
        #entry pod czas rozpoczecia umowy
        self.e_startingdate = Entry(self.rootofviewsignup)
        self.e_startingdate.grid(column = 1, row=9)
        #checking if the startingdate  was written correctly
        self.e_startingdate.bind("<KeyRelease>",self.check_entry_startingdate)
        #########################

        #label pod czas zakonczenia umowy
        self.l_expirationdate = Label(self.rootofviewsignup,text="Czas zakonczenia:")
        self.l_expirationdate.grid(column = 0,row=10, pady=10,padx=10)
        #entry pod czas zakonczenia umowy
        self.e_expirationdate  = Entry(self.rootofviewsignup)
        self.e_expirationdate.grid(column = 1,row=10)
        #checking if the expirationdate  was written correctly
        self.e_expirationdate.bind("<KeyRelease>",self.check_entry_expirationdate)
        ###########################

        #button pod wyjscie
        self.b_exit = Button(self.rootofviewsignup,text="Wyjdź", command=self.rootofviewsignup.destroy)
        self.b_exit.grid(column = 0,  row=11,ipady = 5, ipadx= 10, pady=10,padx=10)

        #button pod zarejestruj sie
        self.b_signup = Button(self.rootofviewsignup,text="Zarejestruj sie", command=self.sign_up)
        self.b_signup.grid(column = 1, row=11, ipady = 5, ipadx= 10, pady=10,padx=10)   

        #label wynik rejestracji
        self.l_result = Label(self.rootofviewsignup,text="",foreground="red")
        self.l_result.grid(column = 0, columnspan=2, row=12)

        self.rootofviewsignup.mainloop()

    def hide_show_dates(self,event):
        if(self.c_type.current()==1):
            self.l_expirationdate.grid_forget()
            self.e_expirationdate.grid_forget()
           
        else:
            self.l_expirationdate.grid(column = 0, row=10, pady=10)
            self.e_expirationdate.grid(column = 1,row=10)
            
        if self.c_type.current()==2:
            self.l_dayjob.grid_forget()
            self.c_dayjob.grid_forget()
        else:
            self.l_dayjob.grid(column = 0, row=8, pady=10,padx=10)
            self.c_dayjob.grid(column = 1, row=8,  padx=10)

    def check_entry_login(self,event):
        #print(self.e_login.get())
        self.l_result["text"]=self.viewsignupmodel.check_entry_login(self.e_login.get())

    def check_entry_firstname(self,event):
        
        self.l_result["text"] = self.viewsignupmodel.check_entry_firstname(self.e_firstname.get())

    def check_entry_lastname(self,event):
        self.l_result["text"] = self.viewsignupmodel.check_entry_lastname(self.e_lastname.get())
    
    def check_entry_email(self,event):
        self.l_result["text"] = self.viewsignupmodel.check_entry_email(self.e_email.get())

    def check_entry_passwd(self,event):
        self.l_result["text"] = self.viewsignupmodel.check_entry_passwd(self.e_passwd.get())

    def check_entry_companyname(self,event):
        self.l_result["text"] = self.viewsignupmodel.check_entry_companyname(self.e_companyname.get())
  
    def check_entry_hourlyrate(self,event):
        self.l_result["text"] = self.viewsignupmodel.check_entry_hourlyrate(self.e_hourlyrate.get())

    def check_entry_startingdate(self,event):
        self.l_result["text"] = self.viewsignupmodel.check_entry_startingdate(self.e_startingdate.get())
    
    def check_entry_expirationdate(self,event):
        self.l_result["text"] = self.viewsignupmodel.check_entry_expirationdate(self.e_expirationdate.get())


    def sign_up(self):
        #checking if the label  result contains rejestracja udana 
        #veryfing that user cant use the button again before he will change login
        if(self.l_result["text"]=="Rejestracja udana"):
            self.check_entry_login(None)
        #if we doesn't have errors, then we can do registration
        elif(self.l_result["text"]==""):
        
            result = self.viewsignupmodel.add_person(
                login=self.e_login.get(),
                email = self.e_email.get(),
                passwd = self.e_passwd.get(),
                firstname = self.e_firstname.get(),
                lastname  = self.e_lastname.get(),
                hourlyrate  = self.e_hourlyrate.get(),
                companyname = self.e_companyname.get(),
                type = self.c_type.get(),
                dayjob = self.c_dayjob.get(),
                startingdate = self.e_startingdate.get(),
                expirationdate = self.e_expirationdate.get()
            
            )

           
            self.l_result["text"] = result
            
                