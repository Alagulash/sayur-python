# write a program that prints out a diamond shape using#


n=int(input("Enter the number of rows:"))
#print the top triangle
for i in range(n):
    print(" "*(n-i-1) + "# "*(i-1))
    
  #print the bottom triangle  
for i in range(n-2,-1,-1):
    print( ""*(n-i-1) + "# "*(i+1))    