
import random


class DataBase:
    def __init__(self):
        self.companyInformation = []
        self.size = len(self.companyInformation)

    
    def MianOption(self):
        print("*************************")
        print("Tender Lottery Project : ")
        print("*************************")
        print("1) Register Company ")
        print("2) Show All Company's Information")
        print("3) Search Company's Information")
        print("4) Lottery Tender ")
        print("0) Exit")
        option1 = int(input("Enter Your Option : "))
        return option1

    def CompanyRegistrationData(self):
        self.register = {
            "Name": input("Enter Company Name : "),
            "Owner": input("Enter Company Owner : "),
            "Licence": input("Enter Licence No : ")
        }
        self.companyInformation.append(self.register)

    def ShowCompanyInformation(self):
        size = len(self.companyInformation)
        print("Show Company's Information : ")
        for iteam in range(size):
            print(f"Show Company Information {iteam+1} : {self.companyInformation[iteam]} ")

    def SearchCompanyInformation(self):
        name = input("Enter Company Name to Search: ")
        found = False
        for company in self.companyInformation:
            if company["Name"].lower() == name.lower():
                print(f"Company Found: {company}")
                found = True
                break
        if not found:
            print("Company not found!")

    def Lottery(self):
        winner_index = random.randint(0, len(self.companyInformation) - 1)
        winner = self.companyInformation[winner_index]
        print(f"-> Lottery Winner: {winner['Name']} owned by {winner['Owner']} with Licence No: {winner['Licence']}")
        
        

# Create a class obj, 

company1 = DataBase()

while(True):
    mainOption = company1.MianOption()
    if(mainOption==1):
        # Registration Comapany, 
        print("** Company Registration ** ")
        n = int(input("How many company want-to Register for Lottery : "))
        for iteam in range(n):
            company1.CompanyRegistrationData()
            print("# Registered!!")
    elif(mainOption==2):
        # Show All Company's Information,
        print("** Show Company's Information ** ")
        if not company1.companyInformation:
            print("-> Data Not found!!")
        else:
            company1.ShowCompanyInformation()
    elif(mainOption==3):
        company1.SearchCompanyInformation()
    elif(mainOption==4):
        company1.Lottery()
    elif(mainOption==0):
        # for exit programe, 
        print("Okey ! Good bye...")
        break





