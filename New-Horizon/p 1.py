from random import randint
tn = randint(0,10)
score = 100
'''
for no in range(0,10):
    no = int(input("enter the guessed number: "))
    if no == tn:
        print("you have found the correct number!!!")
        break
    elif no < tn:
        print("Incorrect value, try a larger number\n")
    else:
        print("Incorrect value, try a smaller number\n")
    score = score - 10
else:
    print("GAME OVER, you have used all your trails")
print("Score = ",score)
'''
for no in tn:
    no = int(input("enter the guessed number: "))
    if no == tn:
        print("you have found the correct number!!!")
        break
    elif no < tn:
        print("Incorrect value, try a larger number\n")
    else:
        print("Incorrect value, try a smaller number\n")
    score = score - 10
else:
    print("GAME OVER, you have used all your trails")
print("Score = ",score)
