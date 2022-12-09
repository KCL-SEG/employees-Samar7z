"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def _init_(self, name, contract, salary , hours, is_Commission , commision_Type , commission , contracts_Number ):
        self.name = name
        self.contract = contract
        self.salary = salary
        self.hours = hours
        self.is_Commission = is_Commission
        self.commision_Type = commision_Type
        self.commission = commission
        self.contracts_Number = contracts_Number
        
        

    def get_pay(self):
        pay = 0

        if self.contract == "monthly":
            if self.is_Commission == False:
                pay = self.salary

            elif self.is_Commission and self.commision_Type == "bonus":
                pay = self.salary + self.commission

            else:
                pay = self.salary +  (self.contracts_Number * self.commission)

        elif self.contract == "hourly":
            if self.is_Commission == False:
                pay = self.salary * self.hours

            elif self.is_Commission and self.commision_Type == "bonus":
                pay = (self.salary * self.hours) + self.commission

            else:
                pay = (self.salary * self.hours) +  (self.contracts_Number * self.commission)

        return pay






    def _str_(self):
        describe = ""
        
        if self.contract == "monthly":
            if self.is_Commission == False:
                describe += f'{self.name} works on a monthly salary of {self.salary}.  Their total pay is {self.get_pay()}.'

            elif self.is_Commission and self.commision_Type == "bonus":
                describe += f'{self.name} works on a monthly salary of {self.salary} and receives a bonus commission of {self.commission}.  Their total pay is {self.get_pay()}.'

            else:
                describe += f'{self.name} works on a monthly salary of {self.salary} and receives a commission for {self.contracts_Number} contract(s) at {self.commission}/contract.  Their total pay is {self.get_pay()}.'


        elif self.contract == "hourly":
            if self.is_Commission == False:
                describe += f'{self.name} works on a contract of {self.salary} hours at {self.hours}/hour.  Their total pay is {self.get_pay()}.'

            elif self.is_Commission and self.commision_Type == "bonus":
                describe += f'{self.name} works on a contract of {self.salary} hours at {self.hours}/hour and receives a bonus commission of {self.commission}.  Their total pay is {self.get_pay()}.'

            else:
               describe += f'{self.name} works on a contract of {self.salary} hours at {self.hours}/hour and receives a commission for {self.contracts_Number} contract(s) at {self.commission}/contract.  Their total pay is {self.get_pay()}.'                
        
        return describe



# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie')

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie')

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee')

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan')

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie')

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel')
