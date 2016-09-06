# Assignment 3 by Marcus Lindstedt Malmö Högskola

# Part 1 User input


def add_name():
    # The function asks for values and adds them to the correct key using user input
    # In this case first_name is the key for the value last_name.
    print("Enter first name: ")
    first_name = input()
    print("Enter last name: ")
    last_name = input()
    my_person_list[first_name] = last_name

my_person_list = {}

while True:
    # I chose to use a given input to exit instead of the else statement used in the example
    # I made this choice to remove the risk of accidentially closing the application due to
    # a hasty error.
    choice = input("Chose: (1) Add person, (2) List all, (3) to exit the program\n")

    if choice == "1":
        add_name()

    if choice == "2":
        for i in my_person_list:
            print(i, my_person_list[i])

    if choice == "3":
        break


# Uppgift 2 Reading and writing to files

player_file = open("players.txt", "w")

player_list = {}


def add_player(first_name, last_name, country):
    print("Enter first name: ")
    first_name = input()
    player_list["first_name"] = first_name
    print("Enter last name: ")
    last_name = input()
    print("Enter country you represent: ")
    country = input()

    player_file.write(first_name, last_name, country)
    player_file.close()


def print_players():
    for player in player_file:
        print(player, player_file[player])


def start():
    while True:
        choice = input("Chose: (1) Add person, (2) List all, (3) to exit the program\n")

        if choice == "1":
            add_player()

        if choice == "2":
            for i in my_person_list:
                print(i, my_person_list[i])

        if choice == "3":
            break
start()
