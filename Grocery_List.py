# Grocery list

print('Welcome to your grocery list!')

# prompt user to create a shopping list
list1 = input('Enter items to pick up at the grocery store separated by space: ')
grocery_list = list1.split(" ")

# while loop as long as there are items and a for loop to iterate through list
while len(grocery_list) > 0:
    print('\nHere is your list: ')
    for i in grocery_list:
        print(i)

    # check off items as you go
    user_input = input("\nPlease type in item found: \n").lower()
    if user_input in grocery_list:
        grocery_list.remove(user_input)

    # don't buy outside your list
    else:
        print("***Please stick to the list***")

print("\nCONGRATULATIONS YOU ARE NOW DONE WITH GROCERY SHOPPING!!!")


