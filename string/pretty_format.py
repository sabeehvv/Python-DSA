def pretty_format(string,width):
    words = string.split()
    current_word = ""
    formated_word = ""

    for word in words:
        if len(current_word + word) <= width:
            current_word += word + " "
        else:
            formated_word += current_word.split() + "\n"
            current_word = word + " "

    formated_word += current_word.split()

    return formated_word