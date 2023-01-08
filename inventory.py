
from tabulate import tabulate

#========The beginning of the class==========
class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        """Initialise the following attributes:
        country, code, product, cost and quantity."""
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    def get_country(self):
        """ Return country. """
        return self.country

    def get_code(self):
        """ Return code. """
        return self.code

    def get_product(self):
        """ Return prodact's name. """
        return self.product

    def get_cost(self):
        """ Return the cost of the shoe. """
        return self.cost

    def get_quantity(self):
        """ Return the quantity of the shoes. """
        return self.quantity

    def __str__(self):
        """ Returns a string representation of a class. """
        return f"""Country:  {self.country}
Code:     {self.code}
Product:  {self.product}
Cost:     {self.cost}
Quantity: {self.quantity}
"""

#=============Shoe list===========

shoe_list = []                       # The list will be used to store a list of objects of shoes.
header = []
#==========Functions outside the class==============
def read_shoes_data(name_file):
    """ This function will open the file inventory.txt and read the data from this file,
    then create a shoes object with this data and append this object into the shoes list.
    One line in this file represents data to create one object of shoes. """
    try:
        with open(name_file, "r", encoding="utf-8") as f1:
            list_of_lines = f1.readlines()
            header.extend(list_of_lines[0].strip().split(","))
            for line in list_of_lines[1:]:
                stock = line.strip().split(",")
                shoe = Shoe(country=stock[0], code=stock[1], product=stock[2], cost=float(stock[3]), quantity=int(stock[4]))
                shoe_list.append(shoe)
    except IOError:
        print("Error: failed to open file.")

def capture_shoes():
    """ This function will allow a user to capture data about a shoe and use this data 
    to create a shoe object and append this object inside the shoe list. """

    while True:
        country = input("Country: ")
        if "," in country:
            print("Unacceptable symbol in Country name - ','. Re-enter again")
            continue
        else:
            break
    while True:
        code = input("Code: ")
        if "," in code:
            print("Unacceptable symbol in Code name - ','. Re-enter again")
            continue
        else:
            break
    while True:
        product = input("Product: ")
        if "," in code:
            print("Unacceptable symbol in Code name - ','. Re-enter again")
            continue
        else:
            break
    while True:
        try:
            cost = float(input("Cost: "))
            break
        except ValueError:
            print("Wrong entry. Re-enter cost of product, please.")
    while True:
        try:
            quantity = int(input("Quantity: "))
            break
        except ValueError:
            print("Wrong entry! Re-enter quantity, please.")
    new_shoe = Shoe(country=country, code=code, product=product, cost=cost, quantity=quantity)
    shoe_list.append(new_shoe)
    print(f"""New shoes added :
{new_shoe}.""")

def view_all():
    """ This function will iterate over the shoes list and print the details of the shoes returned from the __str__ function.
    Optional: you can organise your data in a table format by using Python’s tabulate module. """
    shoe_list_of_lists = []

    for i in shoe_list:
        shoe = []
        shoe.append(i.country)
        shoe.append(i.code)
        shoe.append(i.product)
        shoe.append(i.cost)
        shoe.append(i.quantity)
        shoe_list_of_lists.append(shoe)

    print(tabulate(shoe_list_of_lists, headers=header))

def re_stock():
    """ This function will find the shoe object with the lowest quantity, which is the shoes that need to be re-stocked.
    Ask the user if they want to add this quantity of shoes and then update it.
    This quantity should be updated on the file for this shoe. """
    min_quantity = shoe_list[0].get_quantity()
    shoe = shoe_list[0]
    for i in shoe_list[1:]:
        if i.get_quantity() < min_quantity:
            min_quantity = i.get_quantity()
            shoe = i
    print(f"""\nShoes with min quantity is:
{shoe}
""")

    while True:
        add = input("Do you want to add this quantity of shoes? yes/no: ")
        if add.lower() == "yes":
            while True:
                num_adding = int(input("How much do you want to add: "))
                try:
                    shoe.quantity += num_adding
                    rewrite_file("inventory.txt")
                    print(f"""
Quantity has been successfully increased:
{shoe}""")
                    return shoe
                except ValueError:
                    print("Invalid input. Try again, please")
        elif add.lower() == "no":
            return shoe
        else:
            print("Wrong choice, please try again")

def rewrite_file(name_file):
    """ This function will rewrite inventory.txt to save all changes have been made """
    with open(name_file, "w+", encoding = "utf-8") as f_1:
        f_1.write("Country,Code,Product,Cost,Quantity")
        for i in shoe_list:
            line = f"\n{i.country},{i.code},{i.product},{i.cost},{i.quantity}"
            f_1.write(line)

def search_shoe(code_number):
    """ This function will search for a shoe from the list using the shoe code
    and return this object so that it will be printed. """
    for i in shoe_list:
        if i.code == code_number.upper():
            return i
    return None

def view_codes():
    """ This function prints out Shoes codes. """
    list_of_codes = []
    for i in shoe_list:
        code_list = []
        code_list.append(i.country)
        code_list.append(i.product)
        code_list.append(i.code)
        list_of_codes.append(code_list)
    print(tabulate(list_of_codes, headers=["Country", "Product", "Code"]))

def value_per_item():
    """ This function calculate the total value for each item. 
    The formula for value: value = cost * quantity. 
    Print this information on the console for all the shoes. """
    list_of_values = []
    for i in shoe_list:
        value_list = []
        value = i.cost * i.quantity
        value_list.append(i.country)
        value_list.append(i.product)
        value_list.append(value)
        list_of_values.append(value_list)
    print(tabulate(list_of_values, headers=["Country", "Product", "Value"]))

def highest_qty():
    """ Write code to determine the product with the highest quantity 
    and print this shoe as being for sale. """
    max_quantity = 0
    for i in shoe_list:
        if i.get_quantity() > max_quantity:
            max_quantity = i.get_quantity()
            shoe = i
    print(f"""Shoes with max quantity is :
{shoe}.""")

def most_expensive():
    """ Find max element in the list_of_cost, identify indext of this element
    and return corresponding Shoe object from shoe_list. """
    list_of_cost = []
    for i in shoe_list:
        list_of_cost.append(i.get_cost())
    max_price = max(list_of_cost)
    index_max_price = list_of_cost.index(max_price)
    return shoe_list[index_max_price]

#==========Main Menu=============

read_shoes_data("inventory.txt")

while True:
    menu = input("""Please choose:
    1 - view details of all items
    2 - add new shoe to warehouse 
    3 - re-stock shoes
    4 - search shoe by code
    5 - total value for items
    6 - show product with the higest quantity
    7 - show the most expensive shoes
    q - exit
    : """)

    if menu == "1":
        view_all()

    elif menu == "2":
        capture_shoes()

    elif menu == "3":
        re_stock()

    elif menu == "4":
        menu_2 = input("""Please choose: 
                       c - enter code
                       s - show all shoes codes
                       0 - exit to main menu
                       :""")
        if menu_2.lower() == "c":
            while True:
                shoe_code = input("\nEnter shoe code or enter 0 to exit to main menu: ")
                if shoe_code == "0":
                    break
                else:
                    if search_shoe(shoe_code) is not None:
                        print(shoe_code)
                    else:
                        print(f"No shoes with {shoe_code} code.")
        elif menu_2.lower() == "s":
            view_codes()
        elif menu_2.lower() == "q":
            break
        else:
            print("Incorrect input. Try again.")

    elif menu == "5":
        value_per_item()

    elif menu == "6":
        highest_qty()

    elif menu == "7":
        max_price = most_expensive()
        print(f"""The most expensive shoes: 
{max_price}""")

    elif menu == "q":
        rewrite_file("inventory.txt")
        print("Goodbye!")
        break

    else:
        print("Incorrect input. Try again.")
