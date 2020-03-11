#BLL
obj = []
c = -1
class CustomerManagementSystem:
    """ this class will be used to store the data of the customers and will 
         modify and display the data when the particular function is called."""
    
    def __init__(self):
        self.id = 5
        self.age = 0
        self.name = 0
        self.mobno = 0
        self.amobno = 0
        self.email = 0
    
    def checkId(self,newid):# 0 if id already available 1 if new id
        for i in range(len(obj)):#for i in obj will also work in this case we can use i instead of obj[i].
            if(obj[i].id == newid):
                return 0
        return 1
    
    def checkAge(self,newage):# 1 if age is between 0 to 100 0 if otherwise
        if(newage > 0 and newage < 100):
            return 1
        else:
            return 0
        
    
    def addCust(self,id,age,name,mobno,amobno,email):
        self.id = id
        self.age = age
        self.name = name
        self.mobno = mobno
        self.amobno = amobno
        self.email = email
    
    def searchCust(self,newid):#returns -1 if not found returns index if found
        for i in range(len(obj)):
            if(obj[i].id == newid):
                return i
        return -1
    
    def delCust(self,newid):
        k = 0
        for i in range(len(obj)):
            if(obj[i].id == newid):
                obj.pop(i)
                obj[i].display()
                k+=1
                break
        if(k == 0):
            print("Customer not found")
            
            
    def modCust(self,age,name,mobno,amobno,email):
        self.age = age
        self.name = name
        self.mobno = mobno
        self.amobno = amobno
        self.email = email
        
    def getIndex(self,newid):
        for i in range(len(obj)):
            if(obj[i].id == newid):
                return i
        return -1
    
    def display(self):
        print("_________________________________________________________________")
        print("Customer Id                :",self.id)
        print("Customer Age               :",self.age)
        print("Customer Name              :",self.name)
        print("Customer Mobile No.        :",self.mobno)
        print("Customer Alternate Mob No. :",self.amobno)
        print("Customer Email             :",self.email)
        print("_________________________________________________________________")
        
#PL
if(__name__ == "__main__"):
    print("***** Welcome to Customer Management System *****")
    while(1):
        print()
        print(" Please enter : ","1 to add Customer ","2 to delete Customer ",
              "3 to search Customer ","4 to modify Customer ","5 to Exit Customer Management System ",sep='\n')
        
        ch = int(input())
        
        if(ch == 1):
            obj.append(CustomerManagementSystem())
            c+=1
            while(1):
                id = input("Enter the id for the customer : ")
                k = obj[c].checkId(id)
                if(k == 0):
                    print(" Id already available please try again. ")
                    continue
                else:
                    break
            while(1):
                age = input("Enter the age of the customer : ")
                age = int(age)
                k = obj[c].checkAge(age)
                if(k == 0):
                    print("Age must be between 0 to 100 please try again. ")
                    continue
                else:
                    break
            name = input("Enter customer name : ")
            mobno = input("Enter customer mobile number : ")
            print("Do you want to give an alternate mobile Number (press 1 for yes 2 for no) : ")
            t = int(input())
            if(t == 1):
                amobno = input("Enter the alternate contact number : ")
            elif(t == 2 ):
                amobno = "Unavailable"
                print("You can add your alternate mobile number later")
            else:
                print("Invalid input Altenate mobile number skipped")
            
            email = input("Enter customer email adress (example: example@gmail.com) : ")
            
            obj[c].addCust(id,age,name,mobno,amobno,email)
            print("Customer added sucessfully :) ")
            obj[c].display()
                
        elif(ch == 2):
            if(c == -1):
                print("Underflow Condition (No Customer to delete).")
            else:
                id = input("Enter the Id of the customer to be deleted : ")
                obj[0].delCust(id)
                print("Customer deleted sucessfully :) ")
                
        elif(ch == 3):
            if(c == -1):
                print("Underflow Condition (No Customer to Search).")
            else:
                id = input("Enter the Id of the customer to be searched : ")
                k = ob[0].getIndex(id)
                if(k == -1):
                    print("No customer with such Id ")
                else:
                    obj[k].display()
                
        elif(ch == 4):
            if(c == -1):
                print("Underflow Condition (No Customer to Modify).")
            else:
                id = input("Enter the Id of the customer to be modified : ")
                l = obj[0].getIndex(id)
                if(l == -1):
                    print("No customer with such Id ")
                else:
                    while(1):
                        age = input("Enter the age of the customer : ")
                        age = int(age)
                        k = obj[c].checkAge(age)
                        if(k == 0):
                           print("Age must be between 0 to 100 please try again. ")
                           continue
                        else:
                           break
                    name = input("Enter customer name : ")
                    mobno = input("Enter customer mobile number : ")
                    print("Do you want to give an alternate mobile Number (press 1 for yes 2 for no) : ")
                    t = int(input())
                    if(t == 1):
                       amobno = input("Enter the alternate contact number : ")
                    elif(t == 2 ):
                       amobno = "Unavailable"
                       print("You can add your alternate mobile number later")
                    else:
                       print("Invalid input Altenate mobile number skipped")
                    email = input("Enter customer email adress (example: example@gmail.com) : ")
                    obj[l].modCust(age,name,mobno,amobno,email)
                    print("Customer modified sucessfully :) ")
                    obj[l].display()
                
        elif(ch == 5):
            break
            
        else:
            print("Invalid entry (Must lie within 0 to 5)")
            
    
    
    
    
    
    
    import time
    d = time.localtime()
    import numpy as np
    id = "Dir" + "Y" + str(d[0]) +"M" + str(d[1]) +"D" + str(d[2])
    + "N" + str(int(np.random.rand()* 10**4))
    print(id)
    
    
   