# -*- coding: utf-8 -*-
"""
Created on Wed May 22 11:39:36 2019

@author: KIIT
"""

#BLL
cusID=[]
cusAge=[]
cusName=[]
def addCust(id,age,name):
    cusID.append(id)
    cusAge.append(age)
    cusName.append(name)
def searchCust(id):
    index=cusID.index(id)
    return index
def delCust(id):
    index=cusID.index(id)
    cusID.pop(index)
    cusAge.pop(index)
    cusName.pop(index)
def modifyCust(id, age, name):
    index = cusID.index(id)
    cusName[index]=name
    cusAge[index]=age

#PL
if(__name__=="__main__")
	while(1):
		print("1: Add Customer")
		print("2: Search Customer")
		print("3: Delete Customer")
		print("4: Modify Customer")
		print("5: Display All Customers")
		print("others: Exit")
		choice=input("Enter Choice 1 to 5")
		if(choice=="1"): #Add Customer
			id=input("Enter Customer ID: ")
			age=input("Enter Customer Age: ")
			name=input("Enter Customer Name: ")
			addCust(id,age,name)
			print("Customer added successfully")
		elif(choice=="2"): #Search Customer
			id=input("Enter Customer ID: ")
			index=searchCust(id)
			print("Cust ID: ", id, "Cust Age: ",cusAge[index],"Cust Name: ",cusName[index])
		elif(choice=="3"): #Delete Customer
			id=input("Enter Customer ID: ")
			delCust(id)
			print("Customer Deleted Successfully")
		elif(choice=="4"):#Modify Customer
			id = input("Enter Customer ID: ")
			age = input("Enter Customer Updated Age: ")
			name = input("Enter Customer Updated Name: ")
			modifyCust(id, age, name)
			print("Customer modified successfully")
		elif(choice=="5"): #Display All Customers
			for i in range(len(cusID)):
				print("Cust ID: ", cusID[i], "\t\tCust Age: ",cusAge[i],"\t\tCust Name: ",cusName[i])
		else:
			exit()
