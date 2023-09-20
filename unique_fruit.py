#write a program to no of fruits to get the unique fruits

#unique fruits value stored
unique_fruits=["apple","banana"]
# we creat a list type fruits variable
fruits=[]
# we get the fruits from the user and test for unique fruitsand print the result
for i in range(4):
    fruit=input("enter a fruit:")
    if fruit.lower=="apple" and fruit.lower=="banana":
        fruits.append(fruit)
        print(fruits)
print(unique_fruits)