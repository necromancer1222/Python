x= [1,10,5,2]
ns = int(input("enter the value to search for: "))
index = 0
#USING WHILE
'''
i = 0
while i < len(x):
    if ns == x[i]:
        print("found the number!, at index x[",i,"]")
        break
    i = i+1
else:
    print("value not found")
'''
#OR
#USING FOR IN RANGE
'''
for i in range(0,len(x)):
    if x[i] == ns:
        print("found the number!, at index x[",i,"]")
        break
else:
    print("value not found")
        
'''
# OR
#USING FOR IN EACH
for i in x:
    if i == ns:
        print("found the number!, at index x[",index,"]")
        break
    index = index +1
else:
    print("value not found")
# if no in x:
#X.COUNT
