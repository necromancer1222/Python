#1- def a function
'''
def add1 ():
    x = 10
    y = 20
    res = x + y
    print("add = ",res)
    
add1()
print(x)
'''
#2- call var
'''
def add1 (m,n):
    res = m + n
    print("add = ",res)

x = 10
y = 20

add1(x,y)
'''
#3- return to get the data from a function
'''
def add1 (m,n):
    res = m + n
    return(res)

x = 10
y = 20

z = add1(x,y)

print(z)
'''
# 4- add a default state so you dont get an error
'''
def add1 (m =0, n =0):
    res = m + n
    return(res)

x = 10
y = 20

z = add1(x)

print(z)
'''
# 5- to overcome the arangement of the varibles
'''
def add1 (m =0, n =0):
    res = m + n
    return(res)

x = 10
y = 20

z = add1( n =y, m =x )

print(z)
'''
# 6- to return more than one var
'''
def add1 (m =0, n =0):
    res = m + n
    res2 = res /2
    return(res,res2)

x = 10
y = 20

z1, z2 = add1( n =y, m =x )

print(z1, z2)
'''
# 7- in list the functions are the same not a copy so you dont  need a return
'''
def add_to_lst(y,n):
    for i in range(0,len(y)):
        y[i] = y[i] + n
        
x = [1,15,5,7]
no = 5

add_to_lst(x,no)
print(x)
'''
# 8- to avoid the x and y from interfering with each other use list.copy()
'''
def add_to_lst(y,n):
    m = y.copy()
    for i in range(0,len(m)):
        m[i] = m[i] + n

    return (m)

x = [1,15,5,7]
no = 5

y = add_to_lst(x,no)

print(x)
print(y)
'''
# 9- global var
def fun():
    global x
    x = 10

