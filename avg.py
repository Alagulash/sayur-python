# student mark avarage proogram using while loop

total=0
no_of_students=5
i=0
while(i< no_of_students):
    student_mark=int(input("Enter your mark:"))
    total+=student_mark
    i+=1
avg=total/5
print("avg is",avg)

