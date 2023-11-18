print("This program is to calculate the payment of the worker")
h = int(input("Please enter the hours of work per day = "))
r = int(input("Enter the payment per hour of the worker = "))

if h > 8:
    ot = h - 8
    n_rate = r*2
    payment = (h * r)+(ot * n_rate)
    print("the payment = ",payment)
else:
    payment = h * r
    print("the payment = ",payment)

