# Periodic Table App - Displaying information about the elements


### FUNCTIONS ###

def display_title_bar():
    # Displays a title bar.

    print("\t*************************************************")
    print("\t***        Periodic Table Application         ***")
    print("\t*************************************************")
    print("\n\n\n\nPlease choose an option:\n\n")
    print("A - for Adding a new element to the periodic table\n")
    print("I - see all the stored Information about an element\n")
    print("P - choose a Property and see that property for all the element\n")
    print("T - see the entire Table\n")
    print("Q - for quiting\n")


def display_periodic_table():
    print(periodic_table)

def add_element():
    # Add a new element to the data base

    # Get the information about the new element from the user
    symbol = input("\nPlease enter the element's symbol\n")

    # Check if this element already exists in the data base
    if symbol in periodic_table.keys():
        print("\nThis element already exists..\n")

    else:
        # Get the properties of the new element
        new_properties = {}
        new_properties["name"] = input("\nPlease enter the name of the element\n")
        new_properties["atomic_number"] = input("\nPlease enter the atomic number of the element\n")
        new_properties["row"] = input("\nPlease enter the row of the element\n")
        new_properties["column"] = input("\nPlease enter the column of the element\n")

        # Add a new element to the data base
        periodic_table[symbol] = new_properties


### MAIN PROGRAM ###
periodic_table = {}
user_choice = ""

while user_choice != "Q":
    display_title_bar()

    user_choice = input("Enter your choice please: ")
    if user_choice == "Q":
        print("Thanks for being with me, bye!")

    elif user_choice == "A":
        add_element()

    elif user_choice == "I":
        # See the information about a specific element
        element_symbol = input("\nEnter the symbol of the element on which you want the information")

    #elif user_choice == "P":
        # See the property for each element in the table

    elif user_choice == "T":
        # See the entire table
        display_periodic_table()

    else:
        # Undefined
        print("Sorry, I couldn't understand your choice")