
for row in range(0,8):
    for column in range(0,8):
        if column%2==0:
            print("\u25A0",end=" ")
        else:
            print("\u25A1",end=" ")
    print()            