#1. The Calculator App

operator = input("Enter an operator (+ - * /): ")
num1 = float(input("Enther the 1st number: "))
num2 = float(input("Enter the 2nd number: "))

if operator == "+":
    result = num1 + num2
    print(round(result), 3)
elif operator == "-":
    result = num1 - num2
    print(round(result, 3))
elif operator == "*":
    result = num1 * num2
    print(round(result, 3))
elif operator == "/":
    result = num1 / num2
    print(round(result, 3))
else:
    print(f'{operator} is not a valid operator')

# 2. The Shopping List Maker

display_list = input("Make your selection")
add_item = input("Add item.")
remove_item = input("Remove item.")
print_formatted_list = ("Print formatted shopping list.")

def mainMenu():
    print ("Shopping List")
           
selection = input("Make your selection: ")
           
if selection == "1":
    display_list()
elif selection == "2":
    add_item()
elif selection == "3":
    remove_item()
else: 
    print("You did not make a valid selection.")

shopping_list = ["apples", "bananas", "carrots", "dates"]
           
def displayList():
    print()
    print("Shopping List")
    
    for i in shopping_list:
        print("* " + i)   

def add_Item():
    item = input("Enter item you wish to add to the shopping list")
shopping_list.append(Item)
print(Item + " has been added to the shopping list.")

def removeItem():
    item = input("Which item would you like to remove from the shopping list?")      
    shopping_list.remove(item)
    print(item + "has been removed from the shopping list.")
mainMenu()

def print_formatted_list(my_list):
    for item in my_list:
        print(f"- {item}")

my_list = [1, 2, 3, 4, 5]
print_formatted_list(my_list)