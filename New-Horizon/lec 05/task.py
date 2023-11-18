from random import randint
tn = randint(1,10)
score = 100
'''
cnt = 10
while cnt > 0:
    gn = int(input("enter the guessed number: \n"))
    if gn == tn:
        print("you found the true number!!!")
        break
    if cnt> 1:
        print("too bad, try again\n")
        if gn>tn:
            print("try a smaller number\n")
        elif gn <tn:
            print("try a lager number\n")
    cnt = cnt - 1
    score = score - 10
if gn != tn:
        print("GAME OVER")
print("Score : ",score)
'''
#or
for no in range(0,10):
    no = int(input("enter the guessed value: "))
    if no == tn:
        print("you have found the correct number!!!")
        break
    elif no < tn:
        print("Incorret value, try a larger number\n")
    else:
        print("Incorret value, try a smaller number\n")
    score = score - 10
else:
    print("GAME OVER, YOU HAVE USED ALL YOUR TRAILS")
print("Score = ", score)
