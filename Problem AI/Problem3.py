'''
// Here Increment is User Input, 

In the Salary list already mention the salaries, 
make a method where works to Increment 10% of salaries, 
print the Main Salaries
print the 10% Increment Salaries,

'''


def IncrementSalary(Salary,incrementAmmount):
    newSalary = []
    for x in range(0,len(Salary)):
        newSalary.append(Salary[x]*incrementAmmount)

    print(f"{incrementAmmount}, new Salary : ",newSalary)



Salary = [15000,20500,50000,12000,30190]
print("Main Salary : ", Salary)
incrementAmmount = float(input("Enter the Increment Ammount : "))
IncrementSalary(Salary,incrementAmmount)