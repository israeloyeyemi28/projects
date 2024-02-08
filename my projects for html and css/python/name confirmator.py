answer = 'yes'
confirmation = ' '
sure = 'mistake'
first_name = input("what is your first name ?:")
last_name = input("what is your last name ?: ")
surname = input("what is your surname?:")
confirmation = input(f"Are you telling me your name is {first_name} {surname} {last_name} :")
print()

if confirmation == sure:
            print("CONFIRMED")
else :
            print("YOU ARE A BLOODY LIAR")
    

