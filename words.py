def print_upper_words(words):
    """
    Print each word on a seperate line and uppercased.   
    """
    for word in words:
        print(word.upper())


def print_upper_words2(words):
    """
    Print each word on a seperate line and uppercased, if it starts with the letter E       
    """
    for word in words:
        if word.startswith("e") or word.startswith("E"):
            print(word.upper())


def print_upper_words3(words, must_start_with):
    """
    Print each word on a seperate line and uppercased, if it starts with given letter(s)       
    """
    for word in words:
        for letter in must_start_with:
            if word.startswith("letter"):
                print(word.upper())
                break
