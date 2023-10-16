# buy choc and cake
# one choc is rs 200
# one cake is rs 150
# get  budget from the user

no_of_cake=0
no_of_choc=0
money=int(input("Enter your budget: rs"))
while(money>=150):
    if(money>200):
        no_of_choc+=1
        money-=200
    else:
        no_of_cake+=1
        money-=150
print("You can buy",no_of_cake,"cakes and",no_of_choc,"chocolates.")     
