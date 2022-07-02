from tkinter import *
from tkinter import ttk
#from matplotlib.figure import Figure
from tkcalendar import *
from DAL.Entity.User import User


#for plot
#import matplotlib.pyplot as plt
#from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class ViewTabs():
    "Class which represents a new window after logged in "    
    def __init__(self,main_view_model,user):
        
        #main declaration
        #region

        #create variable for set main_view_model
        self.mainviewmodel = main_view_model
        #create variable for set a view-model viewtabsmodel
        self.viewtabsmodel = main_view_model.viewtabsmodel
        #get object of user, which already logging in
        self.actualuser = user

        #configuring the main window
        self.rootofviewtabs = Tk()
        #set title of window
        self.rootofviewtabs.title("Salary-managment")
        #minsize and maxsize of window
        #self.rootofviewtabs.minsize(height=600,width=600)
        #self.rootofviewtabs.maxsize(height=700)
        #block changing size of window
        self.rootofviewtabs.resizable(False,False)
        #create notebook based on roofofviewtabs
        self.my_notebook = ttk.Notebook(self.rootofviewtabs)
        #do padding (upper part of window )
        self.my_notebook.pack(pady=15)
        


        #create frame 1
        self.my_frame1 = Frame(self.my_notebook,  bg="green")
        
        #create frame 2
        self.my_frame2 = Frame(self.my_notebook,   bg="pink")

        #create frame 3
        self.my_frame3 = Frame(self.my_notebook, bg="brown")

        #create frame 4
        self.my_frame4 = Frame(self.my_notebook,  bg="white")
        
        #create frame 5
        self.my_frame5 = Frame(self.my_notebook, bg = "white")

        #endregion


        #view region frame - 1
        #region

        #getting firstname
        firstname = self.viewtabsmodel.get_firstname(user)
        #get the dayjob
        self.dayjob = self.viewtabsmodel.get_dayjob(user)

        #configure column to set the weight, which gives us a responsive columns
        my_frame1_rows = 10
        my_frame1_columns = 2
        for i in range(0,my_frame1_columns+1):
            self.my_frame1.columnconfigure(i,weight=1)
        for i in range(0,my_frame1_rows+1):
            self.my_frame1.rowconfigure(i,weight=1)
        
        #Calendar-label - label for welcome user by anem
        self.l_calendar = Label(self.my_frame1,text="Witaj "+firstname,foreground="black",bg="white",font=("Arial",12),borderwidth=2,relief="raised")
        self.l_calendar.grid(row=0,column=0,columnspan=3,sticky="nsew",padx=5,pady=5,ipadx=5,ipady=5) #nsew - filling in each direction 



        #Calendar - special object (it was install by  pip install tkcalendar)
        self.calendar = Calendar(self.my_frame1,selectmod = "day", year=self.today_year(), month=self.today_month(), day=self.today_day(),locale="pl_PL",date_pattern="dd.mm.yyyy")
        self.calendar.grid(row=1,column=0,columnspan=1,rowspan=5,padx=5)
        self.calendar.bind("<<CalendarSelected>>",self.refresh_and_get_hours)
        
        #Date text:wybrana data: 
        self.l_date_d = Label(self.my_frame1,text="Wybrana data: ",width=20,borderwidth=2,relief="solid")
        self.l_date_d.grid(row=1,column=1,columnspan=2, sticky="nsew",padx=5,pady=5)



        #Day-month-year , which show us a chose day
        self.l_date = Label(self.my_frame1,text=self.today(),borderwidth=2,relief="solid")
        self.l_date.grid(row=2,column=1,columnspan=2, sticky="nsew",padx=5,pady=5)


        #text in label "ilosc godzin"
        self.l_hours_i = Label(self.my_frame1,text="Ilość godzin:",borderwidth=2,relief="solid")
        self.l_hours_i.grid(row=3,column=1,columnspan=2,sticky="nsew",padx=5,pady=5)

        #numbers of hours which are written to specific day
        self.e_hours = Entry(self.my_frame1,borderwidth=2,relief="solid",justify="center")
        self.e_hours.grid(row=4,column=1,columnspan=2,sticky="nsew",padx=5,pady=5)

        #button for setting to set specific number of hours to specific day
        self.b_set = Button(self.my_frame1,text="Ustaw", command=self.set_hour_to_date)
        self.b_set.grid(row=5,column=1,rowspan=1,columnspan=1,sticky="nsew",padx=5,pady=5)

        #button for delete the hours from the specific day
        self.b_delete = Button(self.my_frame1,text="Usuń", command=self.delete_hour_from_schedule)
        self.b_delete.grid(row=5,column=2,rowspan=1,columnspan=1,sticky="nsew",padx=5,pady=5)
       
        #creating legend
        l = ['l4 - zwolnienie lekarskie\n',
            'd - dyzuru w danym dniu\n',
            'godzina - ustawienie ilosci']
        # if someone has "zlecenie" then he cant have l4
        if self.dayjob=="-":
            l = l[1::]
        l="".join(l)

        #text label for legend, which describe, which option we can use
        self.l_legend = Label(self.my_frame1,text=l,borderwidth=2,relief="groove",justify="left")
        self.l_legend.grid(row=6,column=0,rowspan=2,columnspan=1,sticky="we",padx=5,pady=5,ipady=5)

        #creating label ilosc godzin
        self.l_month_choosed = Label(self.my_frame1,text="Godziny w miesiącu:")
        self.l_month_choosed.grid(row=6,column=1,columnspan=2,sticky="nsew",padx=5,pady=(5,0),ipady=5)

        #creating label show number of hours in the specific month
        self.l_month_choosed_hours = Label(self.my_frame1,text="-")
        self.l_month_choosed_hours.grid(row=7,column=1,columnspan=2,sticky="nsew",padx=5,pady=(0,5),ipady=5)

        #if someone doesn't have a "zlecenie" then we have to set the specific view
        if self.dayjob!="-":
            #text for label info hours
            self.l_info_hours_text = "Ilość godzin do przepracowania: "
            self.l_info_hours_number = float()
            #info about hours in month the dynamic field
            self.l_info_hours = Label(self.my_frame1,text=self.l_info_hours_text)
            self.l_info_hours.grid(row=8,column=0,columnspan=1,sticky="nsew",padx=(5,5),pady=5,ipady=5)
    

        #creating label ilosc dyzurow
        self.l_month_shift = Label(self.my_frame1,text="Ilość dyżurów: ")
        self.l_month_shift.grid(row=8,column=1,columnspan=1,sticky="nsew",padx=(5,0),pady=5,ipady=5)

        #creating label showing number of shifts, dynamic field
        self.l_month_shift_count = Label(self.my_frame1,text="",justify="left")
        self.l_month_shift_count.grid(row=8,column=2,columnspan=1,sticky="nsew",padx=(0,5),pady=5,ipady=5)



        self.l_overtime_text = "Ilość nagodzin w miesiącu: "
        self.l_overtime_number = float()
        #info about overtiem  in the month
        self.l_overtime = Label(self.my_frame1,text=self.l_overtime_text)
        self.l_overtime.grid(row=9,column=0,columnspan=1,sticky="nsew",padx=(5,5),pady=5,ipady=5)

        #creating label ilosc l4
        self.l_month_leave_sick = Label(self.my_frame1,text="Ilość L4: ")
        self.l_month_leave_sick.grid(row=9,column=1,columnspan=1,sticky="nsew",padx=(5,0),pady=5,ipady=5)

        #creating label showing number of leave sick
        self.l_month_leave_sick_count = Label(self.my_frame1,text="")
        self.l_month_leave_sick_count.grid(row=9,column=2,columnspan=1,sticky="nsew",padx=(0,5),pady=5,ipady=5)
        
        self.text_l_overtime_all_the_time = "Ogólna suma nadgodzin: "
        self.l_overtime_all_the_time = Label(self.my_frame1,text=self.text_l_overtime_all_the_time)
        self.l_overtime_all_the_time.grid(row=10,column=0,columnspan=3,sticky="nsew",padx=5,pady=5,ipady=5)
        
        
        
        #print(dayjob) #debuggging
        # if  someone has a "zlecenie" then he has an another view
        if self.dayjob=="-":
            self.l_overtime.grid_forget()
            self.l_month_leave_sick.grid_forget()
            self.l_month_leave_sick_count.grid_forget()
            self.l_overtime_all_the_time.grid_forget()
            #self.l_info_hours.grid_forget()
            #text for label earned money
            self.l_earned_money_text = "Zarobione pieniądze: "
            self.l_earned_money_number = float()
            self.l_earned_money = Label(self.my_frame1,text=self.l_earned_money_text)
            self.l_earned_money.grid(row=8,column=0,columnspan=1,sticky="nsew",padx=(5,5),pady=5,ipady=5)
        #endregion



        #view region frame - 2
        #region
        #weights
        my_frame2_rows = 11
        my_frame2_columns = 5
        for i in range(0,my_frame2_columns+1):
            self.my_frame2.columnconfigure(i,weight=1)
        for i in range(0,my_frame2_rows+1):
            self.my_frame2.rowconfigure(i,weight=1)

        #set weight for a responsive view in columns, each column is the same
        
        
        #list for objects label, it will contain all labels of schedules
        self.list_days = []
        #the starting page of view
        self.page = 1
        #how much row we want to show
        self.numbers_of_rows = 11

        #self.generate_rows()
        

        #lable for day
        self.l_day = Label(self.my_frame2,text="Rok:\tMiesiąc:\tDzień:\tIlość:",borderwidth=2,relief="solid")
        self.l_day.grid(row=0,column=0,columnspan=4,sticky="nsew",pady=(5,5),padx=(5,0))
       

        #label for filtry only text
        self.l_available_filters = Label(self.my_frame2,text="Dostepne filtry:",borderwidth=2,relief="solid")
        self.l_available_filters.grid(row=0,column=4,columnspan=2,sticky="nsew",padx=5,pady=5)

        #label do wpisania ilości godzin 
        self.l_filter_number_of_hours = Label(self.my_frame2,text="Ilość godzin: ")
        self.l_filter_number_of_hours.grid(row=1,column=4,columnspan=1,sticky="nsew",ipadx=5,padx=(5,0),pady=5)
        #entry pod wpisanie ilosci godzin it is used for filter
        self.e_filter_number_of_hours = Entry(self.my_frame2,width=6)
        self.e_filter_number_of_hours.grid(row=1,column=5,columnspan=1,sticky="nsew",pady=5,padx=(0,5))
        #binding that the value has been changed
        self.e_filter_number_of_hours.bind("<KeyRelease>",self.numbers_of_hours_value_changed)


        #label do wpisania miesiaca
        self.l_filter_month = Label(self.my_frame2,text="Miesiac: ")
        self.l_filter_month.grid(row=2,column=4,columnspan=1,sticky="nsew",ipadx=5,padx=(5,0),pady=5)
        #entry pod wpisanie miseca
        self.e_filter_month = Entry(self.my_frame2,width=6)
        self.e_filter_month.grid(row=2,column=5,columnspan=1,sticky="nsew",pady=5,padx=(0,5))
        #binding that the value has been changed
        self.e_filter_month.bind("<KeyRelease>",self.month_value_changed)



         #label do wpisania ilości godzin
        self.l_filter_year = Label(self.my_frame2,text="Rok: ")
        self.l_filter_year.grid(row=3,column=4,columnspan=1,sticky="nsew",ipadx=5,padx=(5,0),pady=5)
        #entry pod wpisanie ilosci godzin
        self.e_filter_year = Entry(self.my_frame2,width=6)
        self.e_filter_year.grid(row=3,column=5,columnspan=1,sticky="nsew",pady=5,padx=(0,5))
        #binding that the value has been changed
        self.e_filter_year.bind("<KeyRelease>",self.year_value_changed)



        #label for sort just text
        self.l_sort_type = Label(self.my_frame2,text="Sortuj przez: ",borderwidth=2,relief="solid")
        self.l_sort_type.grid(row=4,column=4,columnspan=2,sticky="nsew",padx=5,pady=5)

        self.list_sort = (
            #name #static-name
            
            ["Rok","year"],
            ["Miesiąc","month"],
           ["Ilość godzin","hours"],
           ["",""]
        )

        #combobox, which has options above
        self.c_sort_type = ttk.Combobox(self.my_frame2,width=10,state="readonly",
        values=[
            self.list_sort[0][0],
            self.list_sort[1][0],
            self.list_sort[2][0],
            self.list_sort[3][0]
        ]
        )
        
        self.c_sort_type.grid(row=5,column=4,columnspan=2,sticky="nsew",padx=5,pady=5)
        #binding, that the combox change the selected option
        self.c_sort_type.bind("<<ComboboxSelected>>",self.sort_type_value_changed)


        
        #label for sort order
        self.l_sort_order = Label(self.my_frame2,text="Kolejność: ",borderwidth=2,relief="solid")
        self.l_sort_order.grid(row=6,column=4,columnspan=2,sticky="nsew",padx=5,pady=5)



        #combobox for set an order
        self.list_sort_order = (
            ["Rosnąco",False],
            ["Malejąco",True]
        )
        #combox, which has options above
        self.c_sort_order = ttk.Combobox(self.my_frame2,width=10,state="readonly",
        values=[
            self.list_sort_order[0][0],
            self.list_sort_order[1][0]
           
        ]
        )
        self.c_sort_order.grid(row=7,column=4,columnspan=2,sticky="nsew",padx=5,pady=5)
         #binding, that the combox change the selected option
        self.c_sort_order.bind("<<ComboboxSelected>>",self.sort_order_value_changed)

        #previous page to change to showing page
        self.b_previous_page = Button(self.my_frame2,text="Poprzednia", command=self.page_previous)
        self.b_previous_page.grid(row=8,column=4,columnspan=1,sticky="nsew",padx=5,pady=5)
        #next page to change to showing page
        self.b_next_page = Button(self.my_frame2,text="Następna", command=self.page_next)
        self.b_next_page.grid(row=8,column=5,columnspan=1,sticky="nsew",padx=5,pady=5)

        #label for ilosc godzin przepracowanych
        self.l_number_of_hours_filtered_text = Label(self.my_frame2,text="Ilość przepracowanych godzin: ",borderwidth=2,relief="solid")
        self.l_number_of_hours_filtered_text.grid(row=9,column=4,columnspan=2,sticky="nsew",padx=5,pady=5)

        #label for przeliczona ilosc przepracowanyc godzin
        self.l_number_of_hours_filtered_result = Label(self.my_frame2,text="",borderwidth=2,relief="solid")
        self.l_number_of_hours_filtered_result.grid(row=10,column=4,columnspan=2,sticky="nsew",padx=5,pady=5)



        #endregion
              
        #view region frame - 3
        #region 


        my_frame3_rows = 8
        my_frame3_columns = 7
        for i in range(0,my_frame3_columns+1):
            self.my_frame3.columnconfigure(i,weight=1)
        for i in range(0,my_frame3_rows+1):
            self.my_frame3.rowconfigure(i,weight=1)
       

        
        #Upside

        ###MONTH
         #big text wynagrodzenie roczne
        self.l_salary_monthly_text = Label(self.my_frame3,text="Wynagrodzenie miesięczne", borderwidth=2,relief="solid")
        self.l_salary_monthly_text.grid(row=0,column=0,columnspan=5,padx=(5,5),pady=(5,5),sticky="nsew")

        #lables for contains object to modify
        Frame3_Labels_left = []
        Frame3_Labels_right = []
        #text  przepracowana ...
        self.l_number_of_hours_in_month_text = Label(self.my_frame3,text="Przepracowana ilość godzin:")
        Frame3_Labels_left.append(self.l_number_of_hours_in_month_text)
        #dynamic text!
        self.l_number_of_hours_in_month_value = Label(self.my_frame3,text="x h",width=10)
        Frame3_Labels_right.append(self.l_number_of_hours_in_month_value)
       
        #text  przepracowana ...
        self.l_number_of_shifts_in_month_text = Label(self.my_frame3,text="Przepracowana ilość dyżurów:")
        Frame3_Labels_left.append(self.l_number_of_shifts_in_month_text)
        
        #dynamic text!
        self.l_number_of_shifts_in_month_value = Label(self.my_frame3,text="x razy")
        Frame3_Labels_right.append(self.l_number_of_shifts_in_month_value)

        #text  przepracowana ...
        self.l_number_of_l4_in_month_text = Label(self.my_frame3,text="Ilość L4:")
        Frame3_Labels_left.append(self.l_number_of_l4_in_month_text)
        #dynamic text!
        self.l_number_of_l4_in_month_value = Label(self.my_frame3,text="x razy")
        Frame3_Labels_right.append(self.l_number_of_l4_in_month_value)
        
        #text  suma....
        self.l_amount_of_overtime_text = Label(self.my_frame3,text="Ilość nadgodzin")
        Frame3_Labels_left.append(self.l_amount_of_overtime_text)
        #dynamic text!
        self.l_amount_of_overtime_value = Label(self.my_frame3,text="xxx")
        Frame3_Labels_right.append(self.l_amount_of_overtime_value)


        #text  suma....
        self.l_sum_salary_for_hours_month_text = Label(self.my_frame3,text="Suma za godziny:")
        Frame3_Labels_left.append(self.l_sum_salary_for_hours_month_text)
        #dynamic text!
        self.l_sum_salary_for_hours_month_value = Label(self.my_frame3,text="xxx")
        Frame3_Labels_right.append(self.l_sum_salary_for_hours_month_value)
        
        #text  suma....
        self.l_sum_amount_of_overtime_text = Label(self.my_frame3,text="Suma za nadgodziny")
        Frame3_Labels_left.append(self.l_sum_amount_of_overtime_text)
        #dynamic text!
        self.l_sum_amount_of_overtime_value = Label(self.my_frame3,text="xxx")
        Frame3_Labels_right.append(self.l_sum_amount_of_overtime_value)

        #text  suma....
        self.l_sum_salary_for_shifts_month_text = Label(self.my_frame3,text="Suma za dyżury:")
        Frame3_Labels_left.append(self.l_sum_salary_for_shifts_month_text)
        #dynamic text!
        self.l_sum_salary_for_shifts_month_value = Label(self.my_frame3,text="xxx")
        Frame3_Labels_right.append(self.l_sum_salary_for_shifts_month_value)

        #text  suma....
        self.l_sum_salary_for_l4_month_text = Label(self.my_frame3,text="Suma za L4:")
        Frame3_Labels_left.append(self.l_sum_salary_for_l4_month_text)
        #dynamic text!
        self.l_sum_salary_for_l4_month_value = Label(self.my_frame3,text="xxx")
        Frame3_Labels_right.append(self.l_sum_salary_for_l4_month_value)

        #text  suma....
        self.l_sum_salary_for_all_month_text = Label(self.my_frame3,text="Całkowite wynagrodzenie:")
        Frame3_Labels_left.append(self.l_sum_salary_for_all_month_text)
        #dynamic text!
        self.l_sum_salary_for_all_month_value = Label(self.my_frame3,text="xxx")
        Frame3_Labels_right.append(self.l_sum_salary_for_all_month_value)
        
        
        #self.l_sum_salary_for_all_month_value.grid(row=7,column=7,columnspan=1,sticky="nsew")

        for i in range(0,len(Frame3_Labels_left)):
            Frame3_Labels_left[i].grid(row=1+i,column=0,columnspan=3,sticky="nsew",padx=5,pady=5,ipadx=5)
            Frame3_Labels_right[i].grid(row=1+i,column=4,columnspan=1,sticky="nsew",padx=5,pady=5,ipadx=5)

        
        
        #down side
        # #label text
        self.l_right_side_text = Label(self.my_frame3,text="Dostępne filtry:",borderwidth=2,relief="solid")
        self.l_right_side_text.grid(row=0,rowspan=1,columnspan=2,column=5,padx=5,pady=5,sticky="nsew")
        # #label text
        self.l_salary_year_text = Label(self.my_frame3,text="Za rok:",borderwidth=2,relief="solid")
        self.l_salary_year_text.grid(row=1,rowspan=1,column=5,padx=5,pady=5,sticky="nsew")
        
        #entry for writing year
        self.e_salary_year = Entry(self.my_frame3,justify="center",width=5)
        self.e_salary_year.grid(row=1, column=6,padx=5,pady=5,sticky="nsew")
        self.e_salary_year.bind("<KeyRelease>",self.calculate_salary)
        
        # #label text Za miesiac
        self.l_salary_month_text = Label(self.my_frame3,text="Za miesiąc:",borderwidth=2,relief="solid")
        self.l_salary_month_text.grid(row=2,column=5,padx=5,pady=5,sticky="nsew")
        #entry for writing month
        self.e_salary_month = Entry(self.my_frame3,justify="center",width=5)
        self.e_salary_month.grid(row=2,column=6,padx=5,pady=5,sticky="nsew")
        self.e_salary_month.bind("<KeyRelease>",self.calculate_salary)

        #label text Stawka za dyzury
        self.l_salary_price_shift_text = Label(self.my_frame3,text="Stawka za dyzury:",borderwidth=2,relief="solid", justify="center")
        self.l_salary_price_shift_text.grid(row=3,column=5,padx=5,pady=5,sticky="nsew")
        #entry for writing price shift
        self.e_salary_price_shift = Entry(self.my_frame3,justify="center",width=5)
        self.e_salary_price_shift.grid(row=3,column=6,columnspan=1,padx=5,pady=5,sticky="nsew")
        self.e_salary_price_shift.bind("<KeyRelease>",self.calculate_salary)

        if self.dayjob=="-":
            self.l_sum_salary_for_l4_month_text.grid_forget()
            self.l_sum_salary_for_l4_month_value.grid_forget()
            
            self.l_sum_amount_of_overtime_text.grid_forget()
            self.l_sum_amount_of_overtime_value.grid_forget()
            
        self.set_default_value()
        self.calculate_salary()
        #endregion

        #view region frame - 4
        #region
        

        #set weight for a responsive view in columns, each column is the same
        # self.my_frame4.columnconfigure(0,weight=1)
        # self.my_frame4.columnconfigure(1,weight=1)
        # self.my_frame4.columnconfigure(2,weight=1)
        # self.my_frame4.columnconfigure(3,weight=1)
        # self.my_frame4.columnconfigure(4,weight=1)
        # self.my_frame4.columnconfigure(5,weight=1)

        # #random data
        # x = [ 1, 2, 3, 4]
        # y = [1, 4, 9 ,16]
        # y2 = [1,2,6,12]

        # #upside is a plot !!
        # self.figure = plt.Figure(dpi=100)
        # self.pl1 = self.figure.add_subplot(111)
        # self.pl1.plot(x,y,color='g')
        # self.pl1.plot(x,y2,color='r')
        # self.pl1.set_title("Wykres wynagrodzeń i ilości \nprzepracowanych godzin w danym okresie")
        # self.pl1.set_xlabel("Okres")
        # self.pl1.legend(["Wynagrodzenie"])

        #self.plot_tk = FigureCanvasTkAgg(self.figure,self.my_frame4)
       #self.plot_tk.get_tk_widget().grid(row=0,column=0,columnspan=5, sticky="nsew",ipady=5)

        #downside are fields
        #text(label)
        # self.l_scale_text = Label(self.my_frame4,text="Skala:",borderwidth=2,relief="solid")
        # self.l_scale_text.grid(row=1,column=0,sticky="nsew",pady=5,padx=5)

        # self.list_scale_options = (
        #     #name #static-name
            
        #     ["Roczna","year"],
        #     ["Miesięczna","month"],
        #    ["Tygodniowa","hours"],
        #    ["Od początku",""]
        # )


        #combox, which has options above
        # self.c_scale_options = ttk.Combobox(self.my_frame4,width=10,state="readonly",
        # values=[
        #     self.list_scale_options[0][0],
        #     self.list_scale_options[1][0],
        #     self.list_scale_options[2][0],
        #     self.list_scale_options[3][0]
           
        # ]
        # )
        # self.c_scale_options.current(3)
        # self.c_scale_options.grid(row=1,column=1,columnspan=2,sticky="nsew",padx=5,pady=5)




        #endregion

        #view region frame - 5
        #region
        my_frame5_rows = 0
        my_frame5_columns = 5
        for i in range(0,my_frame5_columns+1):
            self.my_frame5.columnconfigure(i,weight=1)
        # for i in range(0,my_frame5_rows+1):
        #     self.my_frame5.rowconfigure(i,weight=1)
        
        
        
        self.l_export = Label(self.my_frame5,text="Exporty",width=8,height=1)
        self.l_export.grid(row=0,column=0,columnspan=3,sticky="nsew",padx=5,pady=5)
        
        self.l_date_start = Label(self.my_frame5,text="Data początkowa")
        self.l_date_start.grid(row=1,column=0,columnspan=2,sticky="nsew",padx=5,pady=5)
        
        self.e_date_start = Entry(self.my_frame5,width=7)
        self.e_date_start.grid(row=1,column=2,sticky="nsew",padx=5,pady=5)
        
        self.l_date_end = Label(self.my_frame5,text="Data końcowa")
        self.l_date_end.grid(row=2,column=0,columnspan=2,sticky="nsew",padx=5,pady=5)
        
        self.e_date_end = Entry(self.my_frame5,width=7)
        self.e_date_end.grid(row=2,column=2,sticky="nsew",padx=5,pady=5)
        
        self.l_date_info = Label(self.my_frame5,text="Prawidłowy format daty to: YYYY.MM")
        self.l_date_info.grid(row=4,column=0,columnspan=3,rowspan=1,sticky="nsew",padx=5,pady=5)

        self.b_expor_data_to_file = Button(self.my_frame5,text="Exportuj do pliku", command=self.export_to_file)
        self.b_expor_data_to_file.grid(row=3,column=0,rowspan=1,columnspan=3,sticky="nsew",padx=5,pady=5)


        self.l_settings = Label(self.my_frame5,text="Ustawienia")
        self.l_settings.grid(row=0,column=3,columnspan=3,sticky="nsew",padx=5,pady=5)
        
        self.l_type = Label(self.my_frame5,text="Typ umowy")
        self.l_type.grid(row=1,column=3,columnspan=2,rowspan=1,sticky="nsew",padx=5,pady=5)
        
        self.e_type = Entry(self.my_frame5,width=7)
        self.e_type.grid(row=1,column=5,columnspan=1,rowspan=1,sticky="nsew",padx=5,pady=5)
        
        self.l_startingdate = Label(self.my_frame5,text="Czas rozpoczęcia umowy")
        self.l_startingdate.grid(row=2,column=3,columnspan=2,sticky="nsew",padx=5,pady=5)
        
        self.e_startingdate = Entry(self.my_frame5,width=7)
        self.e_startingdate.grid(row=2,column=5,columnspan=1,rowspan=1,sticky="nsew",padx=5,pady=5)
        
        self.l_expirationdate = Label(self.my_frame5,text="Czas zakończenia umowy")
        self.l_expirationdate.grid(row=3,column=3,columnspan=2,sticky="nsew",padx=5,pady=5)
        
        self.e_expirationdate = Entry(self.my_frame5,width=7)
        self.e_expirationdate.grid(row=3,column=5,columnspan=1,rowspan=1,sticky="nsew",padx=5,pady=5)
        
        
        self.l_hourlyrate = Label(self.my_frame5,text="Stawka na godzine")
        self.l_hourlyrate.grid(row=4,column=3,columnspan=2,sticky="nsew",padx=5,pady=5)
        
        self.e_hourlyrate = Entry(self.my_frame5,width=7)
        self.e_hourlyrate.grid(row=4,column=5,columnspan=2,sticky="nsew",padx=5,pady=5)
        
        self.l_dayjob = Label(self.my_frame5,text="Etat:")
        self.l_dayjob.grid(row=5,column=3,columnspan=2,sticky="nsew",padx=5,pady=5)
        
        self.c_dayjob = ttk.Combobox(self.my_frame5, width=10, state="readonly",
                            values=[
                                    "1/4", 
                                    "1/2",
                                    "3/4",
                                    "Pełny"]
                                    )
    
        self.c_dayjob.grid(row=5,column=5,sticky="nsew",padx=5,pady=5)
        self.c_dayjob.current(0)
        
        self.b_change_settings = Button(self.my_frame5,text="Zapisz ustawienia")
        self.b_change_settings.grid(row=6,column=3,columnspan=2,sticky="nsew",padx=5,pady=5)
        
        
        #endregion

        #packing the frames
        self.my_frame1.pack(fill="both",expand=1)
        self.my_frame2.pack(fill="both",expand=1)
        self.my_frame3.pack(fill="both",expand=1)
        #self.my_frame4.pack(fill="both",expand=1)
        self.my_frame5.pack(fill="both",expand=1)

        #add frame to notebook, and gives them names
        self.my_notebook.add(self.my_frame1, text="Zarządzaj godzinami")
        self.my_notebook.add(self.my_frame2, text="Rozpiska")
        self.my_notebook.add(self.my_frame3, text="Wynagrodzenie")
        #self.my_notebook.add(self.my_frame4, text = "Wykres")
        self.my_notebook.add(self.my_frame5, text = "Export/Ustawienia")

        self.refresh_and_get_hours(event=None)
        self.show_number_of_hours_filtered()
        
        #loop 
        self.rootofviewtabs.mainloop()

    
    #frame 1
    #region
    def refresh_and_get_hours(self,event):

        #changing the text inside the label to date got from calendar
        self.l_date["text"] = self.calendar.get_date()
        #set chose_day based on chose day from calendar widget
        chose_day = self.calendar.get_date()
        #print("-------View-----")
        #print(chose_day)
        #print("-------View------")
        #print(chose_day)
        #delete value from e_hours
        self.e_hours.delete(0,END)
        #insert a new value inside e_hours, based on hours from schedule
        self.e_hours.insert(0,self.viewtabsmodel.get_hours_from_schedule(self.actualuser,chose_day))
        if self.dayjob != "-":
            #number of hours, which is needed to work based on dayjob
            self.l_info_hours_number = self.viewtabsmodel.get_hours_of_working(self.actualuser,chose_day)
            self.l_info_hours["text"] = self.l_info_hours_text+str(self.l_info_hours_number)
        #refresh view data
        self.refresh_view_data(chose_day)
        

    #functions returns full date and parts of date
    def today(self):
        return self.viewtabsmodel.get_today()

    def today_year(self):
        return self.viewtabsmodel.get_today_year()

    def today_month(self):
        return self.viewtabsmodel.get_today_month()

    def today_day(self):
        return self.viewtabsmodel.get_today_day()

    def count_the_overtime_all_time(self):
        overtime = self.viewtabsmodel.get_the_overtime_all_time(self.actualuser)
        self.l_overtime_all_the_time["text"] = self.text_l_overtime_all_the_time + str(overtime)

    def set_hour_to_date(self):
        #get date from calendar widgets
        chose_day = self.calendar.get_date()
        #get hour from widgets e_hours
        hour = self.e_hours.get()
        #settting new hour to specific date
        self.viewtabsmodel.set_hour_to_schedule(self.actualuser,chose_day,hour)
        #after changing refresh view
        self.refresh_view_data(chose_day)


    def delete_hour_from_schedule(self):

        #get date from calendar widget
        chose_day = self.calendar.get_date()
        #use function to delte a schedule, by sending chose_day and user
        self.viewtabsmodel.set_hour_to_schedule(self.actualuser,chose_day,"-")
        #after changing refresh view
        self.refresh_view_data(chose_day)
        #change  the value inside the e_hours
        self.e_hours.delete(0,END)
        self.e_hours.insert(0,"-")


    def refresh_view_data(self,chose_day):

        #calculate the sum of hours in the month
        self.l_month_choosed_hours["text"] = self.viewtabsmodel.get_sum_of_hours(self.actualuser,chose_day)
        #calculate a number of shifts
        self.l_month_shift_count["text"] = self.viewtabsmodel.get_sum_of_shifts(self.actualuser,chose_day)
        #calculate a number of L4
        if self.dayjob!="-":
            self.l_month_leave_sick_count["text"] = self.viewtabsmodel.get_sum_of_leave_sick(self.actualuser,chose_day)
            #calculate a number of overtime
            self.l_overtime_number =  float(self.l_month_choosed_hours["text"])-float(self.l_info_hours_number)
            self.l_overtime["text"] = self.l_overtime_text+str(self.l_overtime_number)
            self.count_the_overtime_all_time()
        else:
            hours = self.l_month_choosed_hours["text"]
            value = self.viewtabsmodel.value_of_earned_money(self.actualuser,hours)
            self.l_earned_money["text"] = self.l_earned_money_text + str(value)+" zł"
            self.l_earned_money_number = value
            
        ### REFRESH ROZPISKA FRAME 2!
        self.generate_rows()
        ### REFRESH FRAME 3!
        self.calculate_salary()


    #endregion

    #frame 2
    #region

    #def for assign the view value to model-view value
    #it's for  sort type changed 
    def sort_type_value_changed(self,event):
        self.viewtabsmodel.change_sort_type_value(
            self.list_sort[
                self.c_sort_type.current()
        ][1]
        )
        self.generate_rows()
        
    #def for assign the view value to model-view value
    #it's for sort order changed
    def sort_order_value_changed(self,event):
        self.viewtabsmodel.change_sort_order_value(
            self.list_sort_order[
                self.c_sort_order.current()
            ][1]
        )
        self.generate_rows()

    #def for assign the view value to model-view value hours
    def numbers_of_hours_value_changed(self,event):
        self.viewtabsmodel.change_filter_hours_value(
            self.e_filter_number_of_hours.get()
        )
        self.generate_rows()
        self.show_number_of_hours_filtered()
       
        
    #def for assign the view value to model-view value month
    def month_value_changed(self,event):
        self.viewtabsmodel.change_filter_month_value(
            self.e_filter_month.get()
        )
        self.generate_rows()
        self.show_number_of_hours_filtered()
  
    #def for assign the view value to model-view value year
    def year_value_changed(self,event):
        self.viewtabsmodel.change_filter_year_value(
            self.e_filter_year.get()
        )
        self.generate_rows()
        self.show_number_of_hours_filtered()
      

    #changing page
    def page_next(self):
        #if the displayed list days are less then max number of rows
        if len(self.list_days)<self.numbers_of_rows:
            #print(len(self.list_days))#debugging
            return
        else:
            #change number page to next
            self.page = self.page + 1
        self.generate_rows()

    #changing page
    def page_previous(self):
        #if the get the first page then we cannot back 
        if self.page==1:
            return
        else:
            #otherwise go back
            self.page = self.page - 1
        self.generate_rows()
    
    #getting the value: sum hours after applied filter
    def show_number_of_hours_filtered(self):
        self.l_number_of_hours_filtered_result["text"] = self.viewtabsmodel.get_sum_hours_after_filter()
    

    def generate_rows(self):
        "function which generates the days with hours of working(one shedule)"
        #firsly we have to try deleting old days
        for i in range(0,len(self.list_days)):
            #delete from grid
            self.list_days[i].grid_forget()
            #delete from view
            self.list_days[i].destroy()
        #forgot about all days, empty list
        self.list_days = []

        i=0
        for schedule in self.viewtabsmodel.get_schedules(self.actualuser,self.page,self.numbers_of_rows):#function returns schedules based on actual user, on page and rows
            #save them to list prepared on the start
            self.list_days.append(
                Label(self.my_frame2,text=schedule,borderwidth=2,relief="solid")

            )
            #set grid for this
            self.list_days[i].grid(row=1+i,column=0,columnspan=4,sticky="nsew",padx=(5,0),pady=(0,5))
            
            i = i + 1
            
        del i
        self.show_number_of_hours_filtered()
    #endregion

    #frame 3
    #region
    def set_default_value(self):
        self.e_salary_year.insert(0,self.today_year())
        self.e_salary_month.insert(0,self.today_month())
        self.e_salary_price_shift.insert(0,60)

    def calculate_salary(self,event=None):
        result = self.viewtabsmodel.calculate_salary(
            self.actualuser,
            self.e_salary_year.get(),
            self.e_salary_month.get(),
            self.e_salary_price_shift.get()
                                                          )
        self.l_number_of_hours_in_month_value["text"] = result["hours"]
        self.l_number_of_shifts_in_month_value["text"] = result["shifts"]
        self.l_number_of_l4_in_month_value["text"] = result["l4"]
        self.l_amount_of_overtime_value["text"] = result["overtime"]
        self.l_sum_salary_for_hours_month_value["text"] = result["hours_money"]
        self.l_sum_amount_of_overtime_value["text"] = result["overtime_money"]
        self.l_sum_salary_for_shifts_month_value["text"] = result["shifts_money"]
        self.l_sum_salary_for_l4_month_value["text"] = result["l4_money"]
        self.l_sum_salary_for_all_month_value["text"] = result["full"]
        
    
    
    #endregion
    
    #frame 5
    #region
    def export_to_file(self):
        starting_month = self.e_date_start.get()
        ending_month = self.e_date_end.get()
    
        r = self.viewtabsmodel.export_hours_to_file(self.actualuser,starting_month,ending_month)
        
    
    #endregion