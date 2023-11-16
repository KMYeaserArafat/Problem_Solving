# Input string containing numbers separated by spaces
input_string = input("Enter a string of numbers separated by spaces: ")

# Split the input string into a list of substrings using space as the delimiter
number_strings = input_string.split()

# Convert the list of number strings to a list of integers
number_list = [int(num) for num in number_strings]

# Print the list of integers
print("List of integers:", number_list)
