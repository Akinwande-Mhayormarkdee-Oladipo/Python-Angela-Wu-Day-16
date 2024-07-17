# from turtle import Turtle, Screen
#
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("green")
# timmy.forward(100)
#
# my_screen = Screen()
# my_screen.exitonclick()

#
# from prettytable import PrettyTable
#
# table = PrettyTable()
#
# table.add_column("name",["Ade", "Blu"])
# table.add_column("age", [22, 21])
# table.align = 'l'
#
#
# print(table)

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

print("Welcome!")
menu = Menu()

is_on = True
while is_on:
    options = menu.get_items()
    drink_type = input(f"Enter your coffee order from ({options}): ").lower()
    print(drink_type)
    available_orders = Menu()
    coffee_machine = CoffeeMaker()
    available_money = MoneyMachine()
    process_on = True
    while process_on:
        if drink_type == "report":
            coffee_machine.report()
            print(available_money.report())
            break
        elif drink_type == "off":
            print("Machine switched off")
            is_on = False
            break
        current_order = available_orders.find_drink(drink_type)
        print(current_order)
        while current_order == None and drink_type != "report":
            print("Invalid order.")
            print("Please select from the list: " + available_orders.get_items())
            drink_type = input("Enter your coffee order: ")
            print(drink_type)
            current_order = available_orders.find_drink(drink_type)
        print(current_order.name)
        print("Order Selected: " + current_order.name)
        resource_check = coffee_machine.is_resource_sufficient(current_order)
        if not resource_check:
            print("Available resources are not sufficient")
            is_on = False
            break
        enough_amount = available_money.make_payment(current_order.cost)
        if enough_amount:
            coffee_machine.make_coffee(current_order)
            print("Order Processed!\n\n")

        process_on = False



