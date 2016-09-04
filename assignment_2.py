# Assignment 2 Marcus Lindstedt Malmö Högskola

# Uppgift 1 Range


def print_numbers(x):
    #  range(x, y) generates numbers starting from x to y.
    #  +1 is needed to get the final value since computers start from 0 and not 1 thus the 5th number
    #  is 4

    for i in range(1, x + 1):
        print(i)

print_numbers(5)


# Uppgift 2 FizzBuzz problem
# The FizzBuzz problem is easily solved using Modulus operator.
# My solution uses string concatenation with all the math happening inside the print call
# I add Foo everytime i is divisible by 3, Bar when it's divisible by 5 and both if both requirements are
# met. If neither requirement is met i is printed

def foo_bar(x):

    for i in range(1, x + 1):
        print("Foo"*(i % 3 == 0) + "Bar"*(i % 5 == 0) or i)

print(foo_bar(15))


# Uppgift 3 Lists

# This is how I would solve it since we have a proper library in Python for this particular problem but I assume we are
# supposed to create our own. For this to work you have to import statistics which is available in Python 3.4 and up

# print(statistics.mean([list]))


def calculate_average(list_to_calculate):
    # The function calculates the sum of all the elements in the list and then divides the sum with the total amount of
    # elements in the list.
    sum_of_list = sum(list_to_calculate)
    length_of_list = len(list_to_calculate)
    average_of_list = sum_of_list / length_of_list

    return average_of_list


numbers = [2, 4, 6, 8]
average = calculate_average(numbers)

print(average)


# Uppgift 4 List of names
# Take a list of names and display all names in the list containing MORE letters than min_length_of_name
def filter_names_by_length(name_list, min_length_of_name):

    temp_list = []
    for x in name_list:
        if len(x) > min_length_of_name:
            temp_list.append(x)
            pass
    return temp_list
    pass


names_to_sort = ["Sherlock", "John", "Eliza", "Joe", "Watson"]

names_above_4 = filter_names_by_length(names_to_sort, 4)
print(names_above_4)

names_above_6 = filter_names_by_length(names_to_sort, 6)
print(names_above_6)


# Uppgift 5 Dictionary

# Dictionary
# 'Key': 'Value' is the syntax.
# The key is used to locate the value.
# If you want Sherlock you merely search for first_name and the datastructure returns the correct
# value, in this case Sherlock.
myself = {"first_name": "Sherlock", "last_name": "Holmes", "Age": 35, "top_3_movies": "Seven, Gone Girl, The Prestige"}

print(myself["first_name"])

print(myself["last_name"])

print(myself["Age"])

print(myself["top_3_movies"])


# Uppgift 6 Dictionary function


person = {"first_name": "Sherlock",
          "last_name": "Holmes",
          "age": 35,
          "top_3_movies": ["Seven", "Gone Girl", "The Prestige"]
          }


def print_person(person_to_print):
    # The function takes a dictionary as an argument and prints the values
    # Result is the empty string that we add information to.
    # Age is an integer and thus has to be converted to string
    # top_3_movies is a list and thus we have to iterate through it and add each one
    result = ""

    result += person_to_print["first_name"] + " " + person_to_print["last_name"] + " "
    result += "(" + str(person_to_print["age"]) + "), "
    result += "Top Movies: "

    for movies in person_to_print["top_3_movies"]:
        result += movies + ", "

    print(result)

print_person(person)



# Uppgift 7 Adding to a Dictionary

def create_person():
