no_of_subject=int(input("enter the no of subject:"))
total_marks=0
for num in range(0,no_of_subject):
    sub_mark=int(input("Enter your sub mark:"))
    total_marks+=sub_mark
average_marks=total_marks/no_of_subject
if average_marks>70:
    grade="first class"
elif  average_marks>60:
    grade="second class"
elif average_marks>50:
    grade="third class"
else:
    grade="faill" 
print ("total mark is:",total_marks)
print("average mark is:",average_marks)
print("grade:",grade)         

                  
                  