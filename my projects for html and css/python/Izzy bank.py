import time, os
while True :
    new_amt = []
    acc_bal = " 509,200 "
    #one = "check account balance"
    #two = "add money"
    #three = "withdraw"
    choice = [ ]
    print(" \033[31m", end = " ")
    print('.'*10, "WELCOME TO IZZY BANK \nTHE MOST RELIABLE BANK IN NIGERIA",'.'*10)
    print()
    print(" \033[39m", end = " ")
    print("WHAT DO YOU WANT TO DO?\nCHECK BALANCE\nADD MONEY\nTRANSFER MONEY\nBUY DATA")
    while True:
        choice = input("what do you want to do\n:")
        if choice  == "1" :
            pin = input(" what is your pin :")
            if pin == "1234":
                print("\033[33m" , end = " " )
                print(f"YOUR ACCOUNT BALANCE AS AT TODAY IS: ${acc_bal :}")
            else:
                forgot_pin = input("forgot  pin? :")
                print("\033[36m" , end = " " )
                print("you pin is :1**4")
                time. sleep(2)
                os. system("clear")
        if choice == "2" :
                new_amt = int(input("how much do you want to add? \n"))
                print('.'* 12,"INITIALIZING",'.'* 12)
                print("done\nYOUR NEW AMOUNT IS: ")
                amt = (new_amt) + (509200) + (50)
                print(f"Your amt is :${amt} + #50 bonus for using Izzy bank")
        if choice == "3" :
            withdraw_amt = int(input("HOW MUCH DO YOU WANT TO WITHDRAW?  \n :"))
            print('.'*19,"INITIALIZING",'.'*12)   
            removed_amt = (509200) - (withdraw_amt)
            print(f"your account balance is now:${removed_amt}")  
        if choice == "4" :
            data_bundle = int(input("how much data do you want to buy?\n50MB for #50\n100MB for #100\n"))
            print('.',"INITIALIZING",'.'*19)
            data_amt_removed = (509200) - (data_bundle)
            print(f"CONGRATULATIONS YOU HAVE RECIEVED FREE 50MB FOR RECHARGING THROUGH IZZY BANK,YOUR NEW ACCOUNT BALANCE IS :{data_amt_removed}")
        if choice == "5" :
            exit_account = input("ARE YOU SURE YOU WANT TO EXIT YOUR ACCOUNT? :")
            if exit_account == "yes":
                print('.'*19,"INITIALIZING",'.'*19)
                print("CLOSED,THANKS FOR USING IZZY BANK")
            else :
                print("YOU ARE STILL USING IZZY BANK ")
                
        