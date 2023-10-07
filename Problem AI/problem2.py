'''
In the Salary list already mention the salaries, 
make a method where works to Increment 10% of salaries, 
print the Main Salaries
print the 10% Increment Salaries,

'''

def IncrementSalary(Salary):
    #10% encrement Salary,
    newSalary = []
    for x in range(0,len(Salary)):
        newSalary.append(Salary[x]*0.7)
    
    return newSalary


Salary = [15000,20500,50000,12000,30190]
print("Main Salary : ",Salary)
print("Increment Salary : ", IncrementSalary(Salary))