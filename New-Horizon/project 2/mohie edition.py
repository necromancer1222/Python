def a_list(name = "",opt= "a", empty= 0):
    handle = open("list.txt",opt)
    if empty == 0:
        handle.write(name+"\n")
    handle.close

def input_st():
    name = input("enter FN LN TREM GPA REG_NUM: ").lower()
    if len(name.split()) == 5:
        return(name)
        print("you have entered: ",name)
    else:
        print("check the input, it must have 5 elements")
        return("error")

def r_list():
    handle = open("list.txt","r")
    stds = handle.read()
    stds = stds.split("\n")
    if "" in stds:
        stds.remove("")
    handle.close
    return(stds)

def print_all(p_list):
    for name in p_list:
        name=name.split()
        print("\nFN:",name[0],"LN:",name[1],"TERM:",name[2],"GPA:",name[3],"REG_NU:",name[4],"\n")

def search(reg,stds):
    for name in stds:
        if reg == name.split()[4]:
            return(name)
    else: 
            return("not found")

def remove(reg,stds):
    name = search(reg,stds)
    if name != "not found":
        stds.remove(name)
        a_list(opt="w",empty=1)
        for line in stds:
            a_list(line)
    return(name)


while True:
    opt=input("\n1-enter new std 2-print all 3-search 4-remove 5-update 6-sort or done to exit: ").lower()
    if opt=="done":
        break
    
    elif opt=="1":
        name = input_st()
        if name != "error":
            a_list(name)
            print("the following was added: ", name)
            
    elif opt=="2":
        p_list = r_list()
        print_all(p_list)
        
    elif opt == "3":
        stds = r_list()
        reg = input("enter REG_NU to search for studnet:")
        name = search(reg,stds)
        print("\nthe student",name , "was found using", reg,"as a reg_num")

    elif opt == "4":
        stds = r_list()
        reg = input("enter REG_NU to remove the studnet:")
        name = remove(reg,stds)
        print("\nthe student",name , "was removed using", reg,"as a reg_num")
       #print("the new list is: ",print(stds))











                
    elif opt == "5":
        u = input("\nplease enter the reg_num of the student you want to update: ")
        for names in stds:             
            if u in names:        
                stds.remove(names)
                name = names
                names = names.split()
                names[2]=input("\nenter the new TERM: ").lower()
                names[3]=input("\nenter the new GPA: ").lower()
                names = " ".join(names)
                stds.append(names)
                print("done the value was updated from", name," ...to.... ",names)
    elif opt == "6":
        opt2 = input("1- sort(a~z),  2- sort(z~a): ")
        print(" ")
        if opt2 == "1":
            stds2 = sorted(stds)
        elif opt2 == "2":
            stds2 = sorted(stds,reverse = True)
        for name in stds2:
            name = name.split()
            print("FN: ", name[0],", LN: ",name[1],", TERM: ",name[2],", GPA: ", name[3],", REG_NUM: ",name[4],"\n")
