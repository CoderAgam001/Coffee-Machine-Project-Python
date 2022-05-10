from data import *

# Print The Welcome Message
print("Welcome to The PyCoffee Shop!")

# Extract the Data
espresso = MENU["espresso"]
latte = MENU["latte"]
cappuccino = MENU["cappuccino"]

quarters_value = 0.25
dimes_value = 0.10
nickels_value = 0.5
pennies_value = 0.1
total_money = 0


def main():
    # Ask the user for what they want
    query = input("\nWhat Would You Like? Espresso/Latte/Cappuccino: ").lower()

    if query == "off":
        print("\nThe Machine Is Curently Under Maintenance! Please Come Back Later.")

    elif query == "report":
        print(f"Water: {resources['water']} ML\nMilk: {resources['milk']} ML\nCoffee: {resources['coffee']} GM")

    else:
        def check_ingredients(query):
            """Function to check if the ingredients are sufficient and dedduct the ingredients from the resources."""
            current_water = resources['water']
            current_milk = resources['milk']
            current_coffee = resources['coffee']

            if query == "espresso":
                if current_water >= espresso['ingredients']['water'] and current_coffee >= espresso['ingredients']['coffee']:
                    current_water -= espresso['ingredients']['water']
                    current_coffee -= espresso['ingredients']['coffee']
                
                else:
                    print("Sorry, we don't have enough ingredients!")

            elif query == "latte" or query == "cappuccino":
                if current_water >= latte['ingredients']['water'] and current_milk >= latte['ingredients']['milk'] and current_coffee >= latte['ingredients']['coffee']:
                    current_water -= query['ingredients']['water']
                    current_coffee -= query['ingredients']['coffee']
                    current_milk -= query['ingredients']['milk']

                else:
                    print("Sorry, we don't have enough ingredients!")
        check_ingredients(query)


        def ask_money():
            """Function to ask the user for the amount of money they have."""
            print("Please enter the amount:")
            quarters = int(input("Quarters: "))
            dimes = int(input("Dimes: "))
            nickels = int(input("Nickels: "))
            pennies = int(input("Pennies: "))
            return quarters, dimes, nickels, pennies


        def calculate_change(quarters, dimes, nickels, pennies):
            """Function to calculate the change."""
            total_change = (quarters * quarters_value) + (dimes * dimes_value) + (nickels * nickels_value) + (pennies * pennies_value)
            return total_change


        run_again = input("\nWould You Like To Make Another Order? (Y/N): ").lower()

        ask_again = True
        while ask_again == True:
            if run_again == "y":
                main()
            
            else:
                print("\nThank You For Using The PyCoffee Shop!")
                ask_again = False
                break
main()