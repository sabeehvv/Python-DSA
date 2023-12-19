def is_palindrome(string):
    string = string.lower().replace(" ","")
    n = len(string)
    palindrome = True
    for i in range(n):
        if string[i] != string[-1-i]:
            palindrome = False
            break
    return palindrome

string = "Malayalam"

print(is_palindrome(string))