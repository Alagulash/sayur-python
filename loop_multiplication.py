#print my table
'''
# Print the following using two for loop
1 * 1 = 1
1 * 2 = 2
1 * 3 = 3
1 * 4 = 4
1 * 5 = 5
2 * 1 = 2
2 * 2 = 4
2 * 3 = 6
2 * 4 = 8
2 * 5 = 10
3 * 1 = 3
3 * 2 = 6
3 * 3 = 9
3 * 4 = 12
3 * 5 = 15
'''
for i in range(3):
    i=int(input("enter the number:"))
    for num in range(1,6):
        print(i,'x',num,'=',num*i)
