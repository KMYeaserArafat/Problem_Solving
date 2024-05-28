import random


class DataBase:
    def __init__(self):
        self.companyInformation = []
    
    def MianOption(self):
        print("*************************")
        print("Tender Lottery Project : ")
        print("*************************")
        print("1) Register Company ")
        print("2) Show All Company's Information")
        print("3) Search Company's Information")
        print("4) Lottery Tender ")
        print("0) Exit")
        try:
            option1 = int(input("Enter Your Option : "))
            if option1 not in [0, 1, 2, 3, 4]:
                raise ValueError
            return option1
        except ValueError:
            print("Invalid option. Please enter a number between 0 and 4.")
            return self.MianOption()

    def CompanyRegistrationData(self):
        register = {
            "Name": input("Enter Company Name : "),
            "Owner": input("Enter Company Owner : "),
            "Licence": input("Enter Licence No : ")
        }
        self.companyInformation.append(register)
        print("# Registered!!")

    def ShowCompanyInformation(self):
        print("Show Company's Information : ")
        for index, company in enumerate(self.companyInformation, start=1):
            print(f"Company Information {index}: {company}")

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
        if not self.companyInformation:
            print("No companies registered for the lottery.")
            return
        winner_index = random.randint(0, len(self.companyInformation) - 1)
        winner = self.companyInformation[winner_index]
        print(f"-> Lottery Winner: {winner['Name']} owned by {winner['Owner']} with Licence No: {winner['Licence']}")


# Create a class object
company1 = DataBase()

while True:
    mainOption = company1.MianOption()
    if mainOption == 1:
        print("** Company Registration ** ")
        try:
            n = int(input("How many companies want to register for Lottery: "))
            if n <= 0:
                raise ValueError
            for _ in range(n):
                company1.CompanyRegistrationData()
        except ValueError:
            print("Please enter a valid number of companies.")
    elif mainOption == 2:
        print("** Show Company's Information ** ")
        if not company1.companyInformation:
            print("-> Data Not found!!")
        else:
            company1.ShowCompanyInformation()
    elif mainOption == 3:
        print("** Search Company's Information ** ")
        company1.SearchCompanyInformation()
    elif mainOption == 4:
        print("** Lottery Tender **")
        company1.Lottery()
    elif mainOption == 0:
        print("Okey! Good bye...")
        break
