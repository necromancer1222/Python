from random import randint
tn = randint(1,10)
cnt = 10
while cnt > 0:
    gn = int(input("enter the guessed number: "))
    if gn == tn:
        print("you found the true number!!!")
        break
    if cnt> 1:
        print("too bad, try again")
    cnt = cnt - 1
if gn != tn:
        print("GAME OVER")
    

