def remove_vowels(string):
    vowels = "aeiouAEIOU"
    result = ""
    for char in string:
        if char not in vowels:
            result += char
    return result


my_string = "Hello, world"
new_string = remove_vowels(my_string)
print(new_string)
