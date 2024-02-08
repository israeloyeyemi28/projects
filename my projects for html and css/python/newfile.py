# This is a meal price calculator
childs_price = float(input('What is the price of the childrens  meal ? : $')) 
adults_price = float(input('What is the price of the adults meal ? : $'))
number_of_children = float(input('How many children were present ? : '))
number_of_adults = float(input('How many adults were present ? : '))
sales_tax = float(input('What is the sales tax ? : $'))
# meal_subtotal=(childs_price*number of children) + (price of adults*number of adults)
print()
meals_subtotal = (childs_price * number_of_children) + (adults_price * number_of_adults)
print(f'The meals subtotal is : $ {meals_subtotal}')
# sales_tax = (subtotal*sales tax rate / 100)
print()
sales_tax = (meals_subtotal * sales_tax / 100)
print(f"The sales tax is ${sales_tax}")
# total price of meal = subtotal + sales_tax
print()
Total_price_of_meal = meals_subtotal + sales_tax
print(f"Total is : ${Total_price_of_meal} ")
print()
payment_amount = float(input('What is your payment amount ? : $'))
#change = payment amount - total amount of meal
print()
change = (payment_amount - Total_price_of_meal)
print(f'Your change is: ${change} ')

#this is d extra stuff 


print('Thanks for buying from us')