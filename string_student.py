
no_of_subject=int(input("enter your no of subject:"))
marks=[]
total=0
failed_sub_marks=[]
for i in range(no_of_subject):
     st_mark=int(input("Enter marks for subject:"))
     marks.append(st_mark)
     if st_mark<=40:
          failed_sub_marks.append(st_mark)
     total+=st_mark
avg=total/no_of_subject
aver=[]
aver.append(avg)
print("average mark",avg)
if failed_sub_marks:
          print("you failed in the following subjects with these marks:",failed_sub_marks)
else:
     print("pass")  
print("marks:",marks)      

            
              


    