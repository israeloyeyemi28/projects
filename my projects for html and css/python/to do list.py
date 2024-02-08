import os, time 
my_agenda = [ ]


def print_list():
    print()
    for item in my_agenda :
        print(item)
        print()
    
while True:
    print("welcome to the to-do list program ")
    menu = input("add or remove or view" )  
    if menu == "add" :
        item = input(" what is next on the agenda ?")
#note that whenever you are dealing with append and pop or remove functions,it is list name .append(item) not item.append(listname) okay.   
        my_agenda.append(item) 
        print("added")
    elif menu == "remove" :
       item = input ("what do you want to remove?:")
       if item in my_agenda :
           my_agenda.remove(item)
           print ("removed")
    elif menu == "view" :
       print("\033[33m" , end = " " )
       print_list( )           
    else :
           print(f"{item} was not in the list ")
   