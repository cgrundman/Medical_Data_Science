# Write three functions:
# 1) print_negative which prints all negative elements of an integer or float input list.
# 2) filter_odd which filters out all of the odd elements of an integer list.
# 3) remove_duplicate which removes all duplicate numbers from an integer list


def print_negative(list_in):
    for value in list_in:
        if value < 0:
            print(value)


def filter_odd(list_in):
    odd_list = []
    for value in list_in:

        if value % 2 != 0:
            odd_list += [value]
    print(odd_list)


def remove_duplicate(list_in):
    seen = set()
    unique = []
    for value in list_in:
        if value not in seen:
            unique.append(value)
            seen.add(value)
    print(unique)


test_list = [1, -2, -3, 4, 5, 6, -7, 8, -9, 6]
print("All of the negative values from this list are:")
print_negative(test_list)
print("the sublist of odd values is:")
filter_odd(test_list)
print("The list after the duplicated have been removed is:")
remove_duplicate(test_list)
