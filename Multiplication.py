#print ****** using formattingprint
#my Tables
#Table 1
#1*1=1
#1*2=2
#1*3=3
#1*4=4
#1*5=5



for i in range(3):
   i=int(input("enter the number:"))
   print("My Tables")
   print("Table",i)
   print("******")   
   for num in range(1,6):
       print(num,'x',i,'=',num*i)