
print("     Hello there, welcome to the shopping carting program !!!.")

# create empty lists to store item names and prices
items = []
prices = []

# create a loop to display the menu and process user input
while prices != 5 :
    print("Please select one of the following:")
    print("1. Add item")
    print("2. View cart")
    print("3. Remove item")
    print("4. Compute total")
    print("5. Quit")
    
    choice = input("Please enter an action: ")
    
    # process user input based on the selected option
    if choice == "1":
        item_name = input("What item would you like to add? ")
        item_price = float(input("What is the price of '" + item_name + "'? : $ "))
        items.append(item_name)
        prices.append(item_price)
        print("'" + item_name + "' has been added to the cart.")
    elif choice == "2":
        print("The contents of the shopping cart are:")
        for i in range(len(items)):
            print(str(i+1) + ". " + items[i] + " - $" + "{:.2f}".format(prices[i]))
    elif choice == "3":
        index = int(input("Which item would you like to remove? ")) - 1
        if index < 0 or index >= len(items):
            print("Invalid index. Please try again.")
        else:
            items.pop(index)
            prices.pop(index)
            print("Item removed.")
    elif choice == "4":
        total = sum(prices)
        print("The total price of the items in the shopping cart is $" + "{:.2f}".format(total))
    elif choice == "5":
        print("Thank you. Goodbye")
        break
    else:
        print("Invalid choice. Please try again.")
        
  
        
      