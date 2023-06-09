def reverse_string(input_str):
    if input_str is None or len(input_str) <= 1:
        return input_str
    
    # Convert the string to a list of characters
    char_list = list(input_str)
    
    # Initialize pointers for the start and end of the string
    start = 0
    end = len(char_list) - 1
    
    # Swap characters from both ends until the pointers meet
    while start < end:
        char_list[start], char_list[end] = char_list[end], char_list[start]
        start += 1
        end -= 1
    
    # Convert the list back to a string
    reversed_str = "".join(char_list)
    
    return reversed_str

# Example usage
string_to_reverse = "Hello, World!"
reversed_string = reverse_string(string_to_reverse)
print(reversed_string)
