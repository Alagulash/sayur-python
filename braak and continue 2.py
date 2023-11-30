
'''
Use For loop, break and continue as needed.
 You need Rs 1000 to go to movie. you are asking your parents for money. your parents give you a
some money. Ask your parents for money until you get Rs1000 or a maximum of 5 times.
Each time they give you some money, you need to print how much money you got so far and print "Thank you.".
Print "Thank you " only if the money is > Rs 10. If money is less than or = Rs 10, don't add it
towards the Rs1000 that you need. Use Continue stmt as needed.
 Print how many times you had to ask your parents to get this money.
'''
total_money=0
ask_count=0
for i in range(5):
    money_given=int(input("enter the money your parents gave you:rs"))
    
    if  money_given <=10:
        print("Sorry,i need more money.")
        continue
    total_money +=money_given
    ask_count +=1
    if total_money >=1000:
        print(f"thank you. you now have rs{total_money}.")
        break
    else:
        print(f"thank you. you now have rs{total_money}.")
print(f"congratulation! you got rs{total_money} by asking your parents{ask_count}times.")        
