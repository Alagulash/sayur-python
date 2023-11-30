# computer will guess a random number
# user has to guess that number for each guess ,print 'high'or 'low'
#eg- computer number-189
#user guess 56-print low
#user guess 678-print high


import random
computerno=random.randint(3,9)
attempt=0
while True:
    user_no=int(input("guess the number between 3 and 9:"))
    if user_no==computerno:
        print("congratulations! youguessed the number correctly.")
        break
    elif user_no< computerno:
        print("try a higher number")
    else:
        print("try a lower number.")
    attempt+=1
print("user gussed the number in attempt","attempts")        