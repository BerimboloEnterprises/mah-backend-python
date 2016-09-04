# Assignment 1 by Marcus Lindstedt Malmö Högskola

# Uppgift 1 Aritmetik

print(5 * 2 < 12)
print(55 != 22)
print(16 / 4 == 4)
print(8 + 2 <=  128)
print(32 * 8 > 255)

# Uppgift 2

name = "Sherlock Holmes"
# len(argument) returns number of characters in the argument string
num_of_chars = len(name)

print(num_of_chars)


# Uppgift3 String Concatenation

part_1 = "The area of the Triangle with a width of "
part_2 = 12
part_3 = " and a height of "
part_4 = 8
part_5 = " is: "
part_6 = (part_2 * part_4) / 2

# str(argument) converts the argument into a string
# the + adds the string on top of the previous string
all_parts = part_1 + str(part_2) + part_3 + str(part_4) + part_5 + str(part_6)

print(all_parts)

# Uppgift 4 String Slicing and manipulation

original = "Tisdag"
burger = "Hamburgare"
terminator = "I'll be back"
learn = "It's Learning"
python = "Python: The Good Parts"

# the [arg:arg] slices the given string. first arg is start of slice and second is end of slice
# negative arg IE -10 works from the end of the string and backwards instead
# .upper() and .lower() converts the string to all upper/lowercase
print(original[:3])
print(burger[3:])
print(terminator[5:])
print(learn[4:].upper())
print(python[-10:].lower())

# Uppgift 5 Functions

# def function_name(arguments): creates a function


def calculate_triangle_area(triangle_width, triangle_height):

    triangle_area = triangle_width * triangle_height * 0.5
    return triangle_area

width = 12
height = 8
area = calculate_triangle_area(width, height)
print(area)

# Uppgift 6 If else Statements

# max_val takes in 2 arguments and return the largest. If they are the same x is returned


def max_val(x, y):
    if x == y:
        return x
    if x > y:
        return x
    else:
        return y

# min_val takes in 2 arguments and return the smallest. If they are the same x is returned


def min_val(x, y):
    if x == y:
        return x
    if x < y:
        return x
    else:
        return y


print(max_val(12, 17))
print(max_val(15, 15))
print(max_val(20, 3))
print(min_val(12, 17))
print(min_val(15, 15))
print(min_val(20, 3))

# Uppgift 7 Modulus operator
# x %(mod) number takes remainder


def is_even(x):

    if x % 2 == 0:

        even = "True"

        return even

    else:

        odd = "False"

        return odd

print(is_even(10))
print(is_even(17))



