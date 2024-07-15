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


from prettytable import PrettyTable

table = PrettyTable()

table.add_column("name",["Ade", "Bolu"])
table.add_column("age", [22, 21])
table.align = 'l'


print(table)