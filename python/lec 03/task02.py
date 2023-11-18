age = int(input("enter age: "))
gender = int(input("enter 0 for male, 1 for female: "))
child = int(input("enter number of childern: "))
pclass = int(input("enter passenger class 1, 2, 3: "))

if (gender == 1 and child < 4) or (gender == 0 and age <10) or (gender == 0 and age < 40 and age > 30 and pclass == 1):
    print("survived")
else:
    print("DIED!!")
