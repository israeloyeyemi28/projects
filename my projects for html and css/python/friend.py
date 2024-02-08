friends = []


name = None

while name != "end":
    name = input("What is the name of your friend ?:")
    
    
    if name != "end":
     friends.append(name)
    
print()
print("/nYour friends are:")    

for friend in friends:
    print(friend)