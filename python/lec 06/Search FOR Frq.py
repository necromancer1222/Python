x= [1,10,5,2,10,5,8,1,15,23,10]
ns = int(input("enter the value to search for: "))
index = 0
#USING WHILE
cnt = 0
'''
i = 0
while i < len(x):
    if ns == x[i]:
        cnt = cnt +1   
    i = i+1

print("The value was repeated ",cnt," times")
'''
#OR
#USING FOR IN RANGE
'''
for i in range(0,len(x)):
    if x[i] == ns:
        cnt = cnt +1   


print("The value ",ns, " was repeated ",cnt," times")
'''  
# OR
#USING FOR IN EACH

for i in x:
    if ns == i:
        cnt = cnt +1
        
print("The value ",ns, " was repeated ",cnt," times")
