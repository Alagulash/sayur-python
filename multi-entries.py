'''
write multiplication table like this
1*1=1
1*2=2
etc.get the number as input
'''

multiplicationnumber=int(input("enter the no:"))
no_of_entries=int(input("How may rows do you want to print:"))
for i in range(1,no_of_entries):
    print(i,"*",multiplicationnumber,"=",i*multiplicationnumber)