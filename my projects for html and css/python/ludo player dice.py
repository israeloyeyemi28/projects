import random, os,time

def roll_dice():
    choice = input("DO YOU WANNA ROLL DICE?")
    while choice != "yes":
        random_number = random.randint(0, 7)
        other_number = random.randint(0,7)
        print(f"YOU ROLLED A {random_number} and a {other_number}")
        break
    else:
        print("program closed") 

roll_dice()           

















