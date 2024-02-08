# This my grade program tha5 ask for your grade


grade = int(input('What is your grade percent? :'))

if grade > 90 :
    letter = "A"
elif grade >= 80 :
    letter = "B"
elif grade >= 70 :
    letter = "C"
elif grade >= 60 :
    letter = "D"
else :
    letter = "F"
# athe sign here indicates what the grade carries ,ie A- or A+
    

sign = " "

last_digit = grade / 10

if last_digit >= 7 :
    sign = " + "
elif last_digit <= 3 :
    sign = " - "
else :
    sign = " "
    
if grade >= 93 :
    sign = " "
    
if letter == " F " :    
    sign = " "
    
    
print(f"Your letter grade is : {letter}{sign} ")   
if grade >= 70 :
        print("congratulations! You passed the class! ") 
        
else :
    print("stay focused and you'll get it next time! ")   
    
print ("God bless you")     