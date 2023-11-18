x = []
while True:
    opt = input("press the number of the option you want to use( 1- add new data 2- print the list 3- search 4- remove 5- sum 6- min&max 7- sorting 8-Exit: ")
    if opt == "8":
        break
    elif opt == "1":
        while True:
            add = input("\nenter the value you want to append or write done to exit: ")
            if add == "done":
                break
            x.append(int(add))
    elif opt == "2":
        print(x,"\n")
    elif opt == "3":
        search = input("\npress 1 for search of existence or 2 for search of occurance: ")
        if search == "1":
            e = int(input("enter the value to search for: "))
            if e in x:
                print(e, "was found\n")
            else:
                print("not in list\n")
        elif search == "2":
            o = int(input("enter the value to search for: "))
            cnt = x.count(o)
            print(o,"was found", cnt,"times\n")
    elif opt == "4":
        re = input("enter the number to remove: ")
        if re in x:
            x.remove(re)
        else:
            print("number not found\n")
    elif opt == "5":
        print("sum = ",sum(x),"\n")
    elif opt == "6":
        print("max = ", max(x),"min =", min(x),"\n")
    elif opt == "7":
        st = input("do you want to sort 1- forward or 2- backword: ")
        if st == "1":
            print(sorted(x),"\n")
        elif st == "2":
            print(sorted(x, reverse = True),"\n")
    
