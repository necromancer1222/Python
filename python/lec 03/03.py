my_money = int(input("how much money do you have: "))
if my_money > 100:
    print("good")
elif my_money <= 100 and my_money > 50:
    print("add cash")
elif my_money <= 50 and my_money >20:
    print("TAKE CARE!!! NEED MORE CASH!!!!!!!!")
else:
    print("TT_TT no money")
