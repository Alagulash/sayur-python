#empty rectangle patten

row=int(input("enter the number of rows:"))
colum=row+2
for i in range(row):
    for j in range(colum):
        if i==0 or i==(row-1) or j==0 or j==(colum-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()            
        