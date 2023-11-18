print("This program is to calculate the payment of the worker")
h = int(input("Please enter the hours of work per day = "))
r = int(input("Enter the payment per hour of the worker = "))
payd = h*r
payw = payd * 7
paym = payd * 30
print("\nThe payment per day =",payd,"\n\nThe payment per week =", payw, "\n\npay per month (30 days) =",paym)
