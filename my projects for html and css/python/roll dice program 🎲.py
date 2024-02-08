import random, time, os 
while True:
    print("WELCOME TO THE ROLLING DICE PROGRAM \nUSED IN PLAYING\nLUDO\nSNAKES AND LADDERS")
    choice = input("ROLL DICE?: ")
    if choice== "y":
        random_number = random. randint(1,6)
        other_number = random. randint(1,6)
        print(f"you rolled a {random_number} and a {other_number}")
        time. sleep(3)
        os. system("clear")
    elif choice == "no":
        break
        
print("program closed")    

