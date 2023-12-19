def count_vowels(string):
    vowels = "aeiou"
    count = 0
    for char in string:
        if char.lower() in vowels:
            count += 1
    return count


my_string = "Hello, world!"
num_vowels = count_vowels(my_string)
print("Number of vowels:", num_vowels)
