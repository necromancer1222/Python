stds=[]
while True:
    opt=input("1-enter new std 2-print all 3-search 4-remove 5-update 6-sort or done to exit:").lower()
    if opt=="done":
        break
    elif opt=="1":
        name=input("enter FN LN TERM GPA REG_NU:").lower()#sherif said 5 3.4 1234
        if len(name.split()) ==5:     #name.split()=["sherif","said","5","3.4","1234"]  len(name.split()) =5
            stds.append(name)
            print("this name added to list:",name)
        else:
            print("you may enterd more or less data than requird..please enter the data in 5 elements FN LN TERM GPA REG_NU:")
    elif opt=="2":
        for name in stds:#['sherif said 5 3.4 1234', 'ahmed hossam 2 3.1 54321']
            name=name.split() #name=["sherif","said","5","3.4","1234"]
            print("FN:",name[0],"LN:",name[1],"TERM:",name[2],"GPA:",name[3],"REG_NU:",name[4],"\n")
    elif opt=="3":
        reg=input("enter REG_NU to search for student:")#reg="54321"
        for name in stds:#['sherif said 5 3.4 1234', 'ahmed hossam 2 3.1 54321']
            if reg in name:
                print(name)
                break
        else:
            print("not found")
    
    elif opt=="4":
        reg=input("enter REG_NU to remove student:")#reg="54321"
        for name in stds:#['sherif said 5 3.4 1234', 'ahmed hossam 2 3.1 54321']
            if reg in name:
                stds.remove(name)
                print("this name is removed:",name)
                break
        else:
            print("not found")
    elif opt=="5":
        reg=input("enter REG_NU to update student:")#reg="54321"
        for name in stds:#['sherif said 5 3.4 1234', 'ahmed hossam 2 3.1 54321']
            if reg in name:
                stds.remove(name)#stds=['sherif said 5 3.4 1234']
                name=name.split()#name=["ahmed","hossam","2","3.1","54321"]
                name[2]=input("enter updated TERM:")#3
                name[3]=input("enter updated GPA:")#3.8 #name=["ahmed","hossam","3","3.8","54321"]
                name=" ".join(name)# name='ahmed hossam 3 3.8 54321'
                stds.append(name)#stds=['sherif said 5 3.4 1234', 'ahmed hossam 3 3.8 54321']
                print("this name is updated:",name)
                break
        else:
            print("not found")
    elif opt=="6":
        opt2=input("1-sort(a-z) 2-sort(z-a):")
        if opt2=="1":
            stds2=sorted(stds)
        elif opt2=="2":
            stds2=sorted(stds,reverse=True)
        for name in stds2:#['sherif said 5 3.4 1234', 'ahmed hossam 2 3.1 54321']
            name=name.split() #name=["sherif","said","5","3.4","1234"]
            print("FN:",name[0],"LN:",name[1],"TERM:",name[2],"GPA:",name[3],"REG_NU:",name[4],"\n")
        
