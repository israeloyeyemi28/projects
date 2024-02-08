gpa = float(input("what is your gpa ?:"))  

lowest_grade = float(input("what is your lowest grade ?:"))


if gpa >= 85  and lowest_grade >= 70:
    honour_roll = True
else :
    honour_roll = False
        
if honour_roll == True:
        print('well done') 
else:
        print('try again')
        
