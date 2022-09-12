# Salary management
## PYTHON, MYSQL, TKINTER, MVVM

## How does it work?
Program calculates number of hours spent in work in specific day.  
Including:
- L4
- Holidays
- Shift
- Normal day

Calculating number of hours to work in month also providing for holidays in working week and weekend.  
Based on polish holidays.

In tabs we can operate on our working hours by
- Filtering by number of hours, month, year
- Ordering results  
- Subdividing our earned money by category


## MYSQL

### Tables:
- User: (for logging)
    - id_user
    - login -> varchar
    - email -> varchar
    - passwd -> varchar
- Contract: (for contact info )
    - id_contract
    - type -> varchar
    - startingdate -> date
    - expirationdate -> date
    - companyname -> varchar
    - dayjob -> varchar
    - hourlyrate -> decimal
- Schedule: (for calculating hours)
    - id_schedule
    - date -> date
    - hours -> varchar
    - id_employee -> unsigned int
- Employee: (for additional info about user)
    - id_employee
    - firstname -> varchar
    - lastname -> varchar

Relationship:
- 1 to 1 User<->Employee # one user is one employee
- 1 to 1 User<->Contract # one user has one contract
- 1 to many Employee<->Schedule # one employee can have many schedules

For representing model in program I created entity for each table.  (DAL/Entity)  
For making queries for each table I created repositories. (DAL/Repository)
Connection settings are located in DAL/DBConnection.py  

## View

### Log in

<img src="https://github.com/Qbason/Salary-managment/blob/main/login.PNG" alt="Sign in/up panel" width="500">

### Registration

<img src="https://github.com/Qbason/Salary-managment/blob/main/signup.PNG" alt="Sign up" width="500">    

### Main window

<img src="https://github.com/Qbason/Salary-managment/blob/main/tab1.PNG" alt="Tab" width="500">

### 2 View

<img src="https://github.com/Qbason/Salary-managment/blob/main/tab2.PNG" alt="Tab" width="500">

### 3 View
<img src="https://github.com/Qbason/Salary-managment/blob/main/tab3.PNG" alt="Tab" width="500">

### 4 View

<img src="https://github.com/Qbason/Salary-managment/blob/main/tab4.PNG" alt="Tab" width="500">

