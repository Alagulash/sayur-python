# empty diamond patten

for row in range(0,7):
    for colum in range(0,7):
        if (row+colum==3) or(colum-row==3) or (row+colum==9) or (row-colum==3):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()            
            