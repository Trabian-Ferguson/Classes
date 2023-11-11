# Program Name: Lab6.py 
# Course: IT1114/Section 01
# Student Name: Trabian Ferguson
# Assignment Number: Lab6.py
# Due Date: 10/08/2023
# Purpose: This program encapsulates data about an office worker. 

class Worker:
    def __init__(self):
        #attr. or variables (features of object)
        self.employee_number = 0
        self.office_number = 0
        self.name = " "
        self.birthday = " "
        self.hoursworked = 0
        self.overtimehours = 0

    def get_employee_number(self):
        #method (behaviors of object)
        return self.employee_number
    
    def set_employee_number(self,x):
        self.employee_number = x
    
    def get_office_number(self):
        return self.office_number
    
    
    def set_office_number(self,x):
        if x < 100 or x > 500:
            return False
        self.office_number = x
        return True

    def get_name(self):
        return self.name

    def set_name(self,x):
        self.name = x
    
    def set_birthdate(self,d,m,y):
        if d < 32 and d > 0:
            if m < 13 and m > 0:
                self.birthday=str(m)+"/"+str(d)+"/"+str(y)
                return True
        return False


    def get_hours_worked(self):
        return self.hoursworked 

    def add_hours(self,x):
        if x > 9:
            self.hoursworked = self.hoursworked + 9 
            self.overtimehours = self.overtimehours + x-9

        else:
            self.hoursworked = self.hoursworked = x
        
    
    def get_hours_overtime(self):
        return self.overtimehours
    



w1 = Worker()
w1.set_office_number(359)




