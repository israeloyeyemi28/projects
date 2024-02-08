#Gooday every one and welcomr to my adventure game, i hope you like it

print("You are walking through a dark forest and find two items: a MATCH and a FLASHLIGHT.")
choice = input("Which one do you want to pick up? (MATCH/FLASHLIGHT) :")
# Dont forget that choice has to be changed to upper() ie;
if choice.upper() == "MATCH":
    print("You pick up the match and strike it to create a small wick of light.")
    time.sleep(2)
    print("You see a path ahead of you, but it's too dark and scary to see very far.")
    print("You can either:")
    print("A) FOLLOW THE PATH WITH YOUR MATCH")
    print("B) STAY WHERE YOU ARE AND WAIT FOR DAYLIGHT")
    choice = input(": ")
    if choice.upper() == "A":
        print("You follow the path with your match, but it quickly fades out.")
        print("You are lost and unable to continue.")
        time.sleep(2)
        print("GAME OVER")
    elif choice.upper() == "B":
        print("You stay where you are and wait for daylight.")
        print("As the sun rises, you are able to see the path more clearly and continue on your journey.")
        time.sleep(2)
        print("CONGRATULATIONS, YOU HAVE SURVIVED THE FOREST!")
    else:
        print("Invalid choice. Try again.")
 # Meaning if the user ttpes a word out of context it should give invalid choice.       
elif choice.upper() == "FLASHLIGHT":
    print("You pick up the flashlight and turn it on.")
    print("You see a path ahead of you, but it's blocked by a fallen tree.")
    print("You can either:")
    print("A) TRY TO MOVE THE TREE")
    print("B) FOLLOW ANOTHER PATH THROUGH THE FOREST")
    choice = input("> ")
    if choice.upper() == "A":
        print("You try to move the tree, but it's too heavy.")
        print("You waste too much time and eventually succumb to hunger and exhaustion.")
        time.sleep(2)
        print("GAME OVER")
    elif choice.upper() == "B":
        print("You follow another path through the forest and eventually come across a stream.")
        print("You can either:")
        print("1) FOLLOW THE STREAM TO LOOK FOR CIVILIZATION")
        print("2) SET UP CAMP AND WAIT FOR RESCUE")
        choice = input("> ")
        if choice == "1":
            print("You follow the stream and eventually come across a small town.")
            time.sleep(2)
            print("CONGRATULATIONS, YOU HAVE SURVIVED THE FOREST!")
        elif choice == "2":
            print("You set up camp and wait for rescue, but no one comes.")
            print("You eventually succumb to hunger and thirst and are unable to continue.")
            time.sleep(2)
            print("GAME OVER")
        else:
            print("Invalid choice. Try again.")
    else:
        print("Invalid choice. Try again.")

else:
    print("Invalid choice. Try again.")
    
# i hope you like it oo    
  
   


