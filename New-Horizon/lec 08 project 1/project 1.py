stds=[]
while True:
    opt=input("\n1-enter new std 2-print all 3-search 4-remove 5-update 6-sort or done to exit: ").lower()
    if opt=="done":
        break
    elif opt=="1":
        name=input("\nenter the FN LN TERM GPA REG_NU: ").lower()
        if len(name.split()) == 5:    
            stds.append(name)
            print("\nthis value was added to list: ",name)
        else:
            print("\nyou may have enterd more or less data than requird ...please re-enter the data in 5 elements FN LN TERM GPA REG_NU: ")
    elif opt=="2":
        for name in stds:
            name=name.split()
            print("\nFN:",name[0],"LN:",name[1],"TERM:",name[2],"GPA:",name[3],"REG_NU:",name[4],"\n")
    elif opt == "3":
        s = input("\nenter the reg_num to search for the student: ")
        for name in stds:
            if s in name:
                print("\nthe student",name , "was found using", s,"as a reg_num")
            else:
                print("not found")
    elif opt == "4":
        re = input("\nplease enter the reg_num of the student you want to remove: ")
        for names in stds:        
            if re in names:     
                stds.remove(names) 
                print("done")
            elif re not in names:
                print("the reg_num", re,"is not in the list")
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
