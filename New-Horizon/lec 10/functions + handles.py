def a_list(name,opt="a"):
    handle = open("list.txt",opt)
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

name = input_st()
if name != "error":
    a_list(name)
