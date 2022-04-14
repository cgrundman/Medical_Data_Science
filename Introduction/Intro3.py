# Write a function printReverseString which takes a sentence under the string format as input (e.g. "Hello world!") and
# prints the sentence with words in the reverse order (e.g. "world! Hello").

def print_reverse_string(string_input):
    str_list = string_input.split()
    rev_list = ' '.join(reversed(str_list))
    print(rev_list)


print_reverse_string('Hello world!')
