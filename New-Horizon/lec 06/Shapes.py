#Square
for row in range(0,5):
    for col in range(0,5):
        print("*",end=" ")
    print()
    
print("\n")

#Triangle Normal
for line in range(1,6):
    for col in range(0,line):
        print("*", end=" ")
    print()

print("\n")

#Triangle Reverse need a hidden arggument
for line in range(5,0,-1):
    for col in range(0,line):
        print("*", end=" ")
    print()
