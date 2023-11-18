def r_std():
    hand = open("test.txt","r")
    stds = hand.read()#read data from H.d(test.txt) and write it on RAM (stds)
    stds = stds.split("\n")#convert string(stds) to list of strings(stds) by using "\n" splitter
    if "" in stds:
        stds.remove("")
    hand.close()
    return(stds)


def w_std(name = "",opt = "a",empty = 0):#name=""  opt="w" empty=1
    hand = open("test.txt",opt)
    if empty == 0:
        hand.write(name+"\n") #enter data #name="ahmed hossam 2 3.5 4561\n" from RAM(name) to H.D(test.txt)
    hand.close()


def enter_std():#enter the data form keyboard to RAM
    name = input("enter FN LN TERM GPA REG_NU:").lower() #enter the data to RAM (name) "ahmed hossam"
    if len(name.split()) == 5:
        return(name)
    else:
        print("you may entrerd....")
        return("wrong")

    
def print_all(stds):
    for name in stds:
        name = name.split()
        print("FN:",name[0],"LN:",name[1],"TERM:",name[2],"GPA:",name[3],"REG_NU:",name[4],"\n")


def search(reg,stds):#stds=['sherif said 5 3.4', 'ahmed hossam 2 3.1 54321', 'mohamed osama 9 3.5 564576']  reg="54321"
    for name in stds:
        if reg == name.split()[4]:#name.split()=["ahmed","hossam","2","3.1","54321"]    name.split()[4]="54321"
            return(name)
    else:
        return("not found")


def remove(reg,stds):
    name = search(reg,stds)#return actual name or "not found"
    if name != "not found":
        stds.remove(name)#remove name from RAM (stds)
        w_std(opt = "w",empty=1)#empty the file
        for line in stds:#write the file again without the removed name
            w_std(line)
    return(name)


def update(reg,stds):
    name=remove(reg,stds)#remove name from file(test.txt) and return actual name  or return "not found"
    if name != "not found":
        name=name.split()
        name[2] = input("enter updated TERM:")
        name[3] = input("enter updated GPA:")
        name = " ".join(name)
        w_std(name)
    return(name)


def sort_std(stds,opt2):
    if opt2 == "1":
        return(sorted(stds))
    else:
        return(sorted(stds,reverse=True))



while True:
    opt=input("1-enter new std 2-print all 3-search 4-remove 5-update 6-sort or done to exit:").lower()
    if opt=="done":
        break
    elif opt=="1":
        name=enter_std()
        if name !="wrong":
            w_std(name)#append
            print("this name addded to the list:",name)
    elif opt=="2":
        stds=r_std()
        print_all(stds)
    elif opt=="3":
        stds=r_std()
        reg=input("enter REG_NU to search for studnet:")
        name=search(reg,stds) #retrun actual name or return "not found"
        print("the name that yousearcehd for:",name)
    elif opt=="4":
        stds=r_std()
        reg=input("enter REG_NU to remove studnet:")
        name=remove(reg,stds) #retrun actual name or return "not found"
        print("the name that removed:",name)
    elif opt=="5":
        stds=r_std()
        reg=input("enter REG_NU to update studnet:")
        name=update(reg,stds) #retrun actual name or return "not found"
        print("the name that you want to update:",name)
    elif opt=="6":
        stds=r_std()
        opt2=input("1-sort(a to z)   2-sort (z to a):")
        stds=sort_std(stds,opt2)
        print_all(stds)
