'''
6.	40 students in a class appeared in their examination. 
Their mark sheets have been given to you that contains student ID, student Name and Grade. 
The grade column of the mark sheet contains the Grade (A, B, C or F) obtained by the student. 
Write a program to calculate the total number of students who got F grade. 
Write a Student class with id, name and grade. 
And Store Data into the txt file whose name is "studentData.txt"

'''

class Student:

    def __init__(self,studentId,studentName,grade) -> None:
        self.studentId = studentId
        self.studentName = studentName
        self.grade = grade


#Here create a list and store data, 
marksSheets = [Student(1,"Anisha","A"),
               Student(2,"John","F"),
               Student(3, "Bruce","C"),
               Student(4,"Linkon","F"),
               Student(5,"Liaf", "B")]

#Function the calculate the total number of F Students 
def count_f_grade(students):
    f_grade_count = 0
    for student in students:
        if student.grade == "F":
            f_grade_count += 1
    
    return f_grade_count


total_f_grade_student = count_f_grade(marksSheets)
print("Total Number of 'F' Grade Students : ", total_f_grade_student)

#Store Data into a text file, 
file1 = open("student.txt","w")
file1.write("Total Number of F Grade Students : " + str(total_f_grade_student))
file1.close()