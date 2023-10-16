number=int(input("enter a number:"))
for i in range(number):
    i=int(input("enter a table number:"))
    print("table",i)
    print("easy number")
    for num in range(1,11):
        print(num,'x',i,'=',num*i)
    print("advance number") 
    for num in range(11,21):
        print(num,'x',i,'=',num*i) 
    print("******")
    print("end of tables")                   