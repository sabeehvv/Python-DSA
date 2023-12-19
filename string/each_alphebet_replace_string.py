def replace_letters(string,n):
    alphebets = "abcdefghijklmnopqrstuvwxyz"
    result = ""
    for char in string:
        if char.isalpha():
            upperecase = char.isupper()
            char = char.lower()
            index = alphebets.find(char)
            new_index = (index + n)%26
            new_char = alphebets[new_index]
            if upperecase:
                new_char = new_char.upper()
            result += new_char
        else:
            result += char
    return result



my_string = "Hello, worlz!"
n = 3
new_string = replace_letters(my_string, n)
print(new_string)



