import os , time, sys
while True :    
    print("welcome to colour animator ")
    run = input("should I run it? ?:")
    if run =="yes" :
        print("colour animator:\n")
        time. sleep(1)
        os. system("clear")
        print("\033[35m" , end = " " )
        print(" purple")
        time. sleep(1)
        os. system("clear")
        print("\033[33m" , end = " " )
        print(" yellow ")
        time. sleep(1)
        os. system("clear")
        print("\033[36m" , end = " " )
        print("light blue")
        time. sleep(1)
        os. system("clear")
        print(" \033[31m", end = " ")
        print("red")
        time. sleep(1)
        os. system("clear")
        print()
        for number in range(1 , 21) :
            print( number , end = "\t" )
        time. sleep(1)
        os. system("clear")
        print()
        print(number , end = "\v")
        time. sleep(1)
        os. system("clear")
        print()
        break
    elif run == "no":
        print("program completed ")
        print()
        break 
    else :
        print(" invalid entry")
        break 