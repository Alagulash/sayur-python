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
       print(i,'x',num,'=',num*i)
       
       
       
'''
  7.Challange questions
Ask the user which tables he/she wants to print (eg 2,9,7,12)
Also ask if they want to see the basic only or advanced only or both.
Hint - use list to get the user input and learn how to use a list in range statement
 '''   