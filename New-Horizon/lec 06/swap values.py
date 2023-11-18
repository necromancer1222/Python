'''
x=10
y=30
z=50
x,y,z = y,z,x
print("x = ",x," y = ",y," z = ",z)
'''

x = [1,10,5,2]
i = 0
print("x = ",x)
x[i],x[i+1] =x[i+1],x[i]
print("x[i] = ",x[i])
print("x[i+1] = ",x[i+1])
print("x = ",x)
