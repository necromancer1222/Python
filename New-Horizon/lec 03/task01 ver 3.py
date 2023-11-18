print("This program is to calculate the payment of the worker")
h = int(input("Please enter the hours of work per day = "))
r = int(input("Enter the payment per hour of the worker = "))

if h > 8:
    ot = h - 8
    ot = ot * 2
    h = 8 + ot
payment = h * r
print("the payment = ",payment)


