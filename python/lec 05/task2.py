from time import sleep
sets = 0
while sets<3:
    cnt = 0
    while cnt<3:
        print("well done!")
        sleep(0.5)
        cnt=cnt+1
    print("rest for 30 sec")
    sets=sets+1
    sleep(5)
print("thats it")
