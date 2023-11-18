x = [1,10,5,2,150]
mx = x[0]

#runs on index

for i in range(0,len(x)):
    if x[i] > mx:
        mx = x[i]
print("max : ", mx)

# runs on a copy of x in i
for i in x:
    if i > mx:
        mx = i
print("max : ", mx)
