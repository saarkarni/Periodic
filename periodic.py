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


def add_all_elements():
    filename = "elements.txt"
    file = open(filename,"r")
    for line in file:
        add_element_from_file(line)


def add_element_from_file(element):
    new_properties = {}
    element_as_list = element.split()

    new_properties["01 - Element Name"] = element_as_list[1]
    new_properties["02 - Atomic Number"] = element_as_list[2]
    new_properties["03 - Row"] = element_as_list[3]
    new_properties["04 - Column"] = element_as_list[4]

    periodic_table[element_as_list[0]] = new_properties


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
        new_properties["01 - Element Name"] = input("\nPlease enter the name of the element\n")
        new_properties["02 - Atomic Number"] = input("\nPlease enter the atomic number of the element\n")
        new_properties["03 - Row"] = input("\nPlease enter the row of the element\n")
        new_properties["04 - Column"] = input("\nPlease enter the column of the element\n")

        # Add a new element to the data base
        periodic_table[symbol] = new_properties


def display_element_information(symbol):
    element_details = periodic_table[symbol]
    for characteristic, value in sorted(element_details.items()):
        print("\n%s:" % characteristic)
        print("%s" % value)


def print_property_for_elements(key):
    for element, properties in periodic_table.items():
            print("\n" + element + ":")
            print(properties[key])


### MAIN PROGRAM ###
periodic_table = {}
add_all_elements()

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
        element_symbol = input("\nEnter the symbol of the element on which you want the information: ")

        if element_symbol not in periodic_table.keys():
            print("Sorry, information is not available")

        else:
            display_element_information(element_symbol)

    elif user_choice == "P":
        # See the property for each element in the table
        print("Available properties are: ")

        # Print the list of available properties - but only once
        for properties in periodic_table.values():
            for property_name in sorted(properties.keys()):
                print(property_name)
            break

        elements_property = input("\nEnter the number of the property which you want to see: ")

        if elements_property == "01":
            print_property_for_elements("01 - Element Name")

        elif elements_property == "02":
            print_property_for_elements("02 - Atomic Number")

        elif elements_property == "03":
            print_property_for_elements("03 - Row")

        elif elements_property == "04":
            print_property_for_elements("04 - Col")

        else:
            print("Sorry, no such property...")


    elif user_choice == "T":
        # See the entire table
        display_periodic_table()

    else:
        # Undefined
        print("Sorry, I couldn't understand your choice")