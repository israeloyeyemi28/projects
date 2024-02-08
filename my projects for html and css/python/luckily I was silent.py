#This program accepts prompts from the user and inserts those words to form a story. It is similar to how a MADLIBS work. 
#used print() to create blank line
print('Please enter the following: ')
print()
adjective=input('adjective: ')
animal=input('animal: ')
verb1=input('verb: ')
exclamation=input('exclamation: ')
verb2=input('verb: ')
verb3=input('verb: ')
print()
print('Your story is: ')
print()
# I used \n to create a new line on the code
output= 'The other day, I was really in trouble. It all started when I saw a very \n' + adjective + ' ' + animal + ' ' + verb1 + ' down the hallway. "' + exclamation.capitalize() + '"! I yelled. But all \nI could think to do was to ' + verb2 + ' over and over. Miraculously, \nthat caused it to stop but not before it tried to ' + verb3 + ' \nright in front of my family.I was quite luck with that, luckily for me i immediately went silent.'
print(output)