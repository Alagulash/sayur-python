'''
get and print the 2 marks each for 3 students.also,get each student name
out put should be
mark 1 for student 1 is 55
mark 2 for student 1 is 67
mark 1 for student 2 is 56
etc

'''

for student in range(1,4):
    student_name=input("Enter the name of student {student}:")
    for mark in range(1,3):
        input_mark=float(input(f"Mark{mark} for {student_name} is:"))
        print(f"Mark{mark}for {student_name}is {input_mark}")