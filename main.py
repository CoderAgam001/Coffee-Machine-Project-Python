from tracemalloc import stop
from data import *

# Print The Welcome Message
print("Welcome to The PyCoffee Shop!")

def main():
    # Extract the Data
    espresso = MENU["espresso"]
    latte = MENU["latte"]
    cappuccino = MENU["cappuccino"]

    quarters_value = 0.25
    dimes_value = 0.10
    nickels_value = 0.5
    pennies_value = 0.01

    ask_again = True
    while ask_again == True:
        # Ask the user for what they want
        query = input("\nWhat Would You Like? Espresso/Latte/Cappuccino: ").lower()
        
        if query == "off":
            print("\nThe Machine Is Curently Under Maintenance! Please Come Back Later.")
            ask_again = False
            break

        elif query == "report":
            print(f"Water: {resources['water']} ML\nMilk: {resources['milk']} ML\nCoffee: {resources['coffee']} GM")

        else:
    
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
                inserted_money = (quarters * quarters_value) + (dimes * dimes_value) + (nickels * nickels_value) + (pennies * pennies_value)
                return inserted_money

            
            def check_money(query):
                """Function to check the money inserted."""
                total_money = 0
                money = ask_money()
                cost = query['cost']
                change = calculate_change(money[0], money[1], money[2], money[3])
                total_money += change

                if change == cost:
                    total_money += change

                elif change < cost:
                    print("\nYou don't have enough money!")
                    print(f"Money Refunded: {change}")
                    total_money -= change

                elif change > cost:
                    print(f"Here is your change: {round(change - cost, 2)}")
                    total_money -= change

                else:
                    if not resources['water'] >= query["ingredients"]["water"] or not resources['milk'] >= query["ingredients"]["milk"] or not resources['coffee'] >= query["ingredients"]["coffee"]:
                        print("We dont have enough money!")
                        print(f"Money Refunded: {change}")


            def make_coffee(query):
                """Function to check if the ingredients are sufficient and make coffee from them."""
                current_water = resources['water']
                current_milk = resources['milk']
                current_coffee = resources['coffee']
                
                # Check if the ingredients are sufficient
                if query == "espresso":
                    if current_water >= espresso["ingredients"]["water"] and current_coffee >= espresso["ingredients"]["coffee"]:
                        current_water -= espresso["ingredients"]["water"]
                        current_coffee -= espresso["ingredients"]["coffee"]

                        check_money(espresso)
                        
                    else:
                        print("\nWe Don't Have Enough Ingredients. Please Try Again Later!")
                
                elif query == "latte":
                    if current_water >= latte["ingredients"]["water"] and current_coffee >= latte["ingredients"]["coffee"] and current_milk >= latte["ingredients"]["milk"]:
                        current_water -= latte["ingredients"]["water"]
                        current_coffee -= latte["ingredients"]["coffee"]
                        current_milk -= latte["ingredients"]["milk"]
                        
                        check_money(latte)

                    else:
                        print("\nWe Don't Have Enough Ingredients. Please Try Again Later!")

                elif query == "cappuccino":
                    if current_water >= cappuccino["ingredients"]["water"] and current_coffee >= cappuccino["ingredients"]["coffee"] and current_milk >= cappuccino["ingredients"]["milk"]:
                        current_water -= cappuccino["ingredients"]["water"]
                        current_coffee -= cappuccino["ingredients"]["coffee"]
                        current_milk -= cappuccino["ingredients"]["milk"]
                        
                        check_money(cappuccino)

                    else:
                        print("\nWe Don't Have Enough Ingredients. Please Try Again Later!")

            make_coffee(query)

        run_again = input("\nWould You Like To Make Another Order? (Y/N): ").lower()
        
        if run_again == "y":
            main()
        
        else:
            print("\nThank You For Using The PyCoffee Shop!")
            ask_again = False
            break
main()