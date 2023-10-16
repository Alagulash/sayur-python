# student mark avarege
# get mark from 5 students and calculate avg


total=0
for i in range(5):
    student_mark=int(input("Enter your mark:"))
    total+=student_mark
avg=total/5
print("avg is",avg)