'''
7.	There are 100 employees in an organization. 
The organization wants to distribute annual bonus to the employees based on their performance. 
The performance of the employees is recorded in their annual appraisal forms. 
Every employee‟s appraisal form contains his basic salary and the grade for his/her performance during the year.
The grade is of three categories – „A‟ for outstanding, „B‟ for good and „C‟ for average performance. 
It has been decided that the bonus of an employee will be 100% of the basic salary for outstanding performance, 
70% of the basic salary for good performance, and 40% of the basic salary for average performance and zero for all other cases.
Write a program to calculate and print the total bonus amount to be distributed by the organization.
 Use Employee class with id, name, salary and performance. employeeData.txt
------------------------------
 tree catagories : 
 A -> outstanding ->100%
 B -> good -> 70%
 C -> average -> 40%
------------------------------

'''

class Employee:

    def __init__(self,id,name,salary,performance) -> None:
        self.id = id
        self.name = name
        self.salary = salary
        self.performance = performance

    def calculate_bonus(self):
        if self.performance == 'A':
            print("Perfomance : OutStanding")
            return self.salary*1
        elif self.performance == 'B':
            print("Performance  : Good")
            return self.salary*0.7
        elif self.performance == 'C':
            print("Performance  : Average")
            return self.salary*0.4
        else:
            return 0



organization = [Employee(1,"Mr.A",150000,'A'),
                Employee(2,"Mr.B",110000,'A'),
                Employee(3,"John", 50000, 'B'),
                Employee(4, "Alice", 60000, 'C'),
                Employee(5, "Bob", 45000, 'C')]
    


total_bonus = 0

file = open("employeeData.txt", "w")


for employee in organization:
    bonus = employee.calculate_bonus()
    total_bonus += bonus
    Dataes = f"Employee ID : {employee.id}, Employee Name : {employee.name}, Salary : {employee.salary}, Bonus : ${bonus}\n"
    #print(f"Employee ID : {employee.id}, Employee Name : {employee.name}, Salary : {employee.salary}, Bonus : ${bonus}")
    print(Dataes)
    file.write(Dataes)
   

total_bonus_Data = "Total Bonus Contribute : " + str(total_bonus)
print(total_bonus_Data)
