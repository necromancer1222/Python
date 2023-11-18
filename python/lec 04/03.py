#finite loop
'''
total = 0
cnt = 0
while cnt < 5:
    pay = int(input("please enter the price of the item: "))
    total = total + pay
    print("Total = ",total)
    cnt = cnt + 1
print("The total money spent = ", total,"$")
'''

#infinte loop

total = 0
while True:
    pay = input("enter the value of the payment OR write done to exit: ")
    if pay == "done":
        break
    total = total + int(pay)
    print(total)
print("Total payment = ", total)
