def find_max_occurrence(input_string):
    char_count = {}
    for char in input_string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    max_char = max(char_count, key=char_count.get)
    max_occurrence = char_count[max_char]

    return max_char, max_occurrence

def find_min_occurrence(input_string):
    char_count = {}
    for char in input_string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    min_char = min(char_count, key=char_count.get)
    min_occurrence = char_count[min_char]

    return min_char, min_occurrence

# Get user input
user_input = input("Enter a string: ")

# Find and remove maximum occurring character
max_char, _ = find_max_occurrence(user_input)
user_input = user_input.replace(max_char, '', )

# Find and remove minimum occurring character
min_char, _ = find_min_occurrence(user_input)
user_input = user_input.replace(min_char, '', )

# Print the modified string
print("Modified string:", user_input)
