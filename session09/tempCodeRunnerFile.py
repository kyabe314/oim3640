# ex-01

def ducklings():
    """
    This function contains given prefixes and suffix for ducks in the book "Make Way for Ducklings" by Robert McClosky. This function will print each duck's name in an alphabetical order.
    """

    prefixes = 'JKLMNOPQ'
    suffix = 'ack'
    for letter in prefixes:
        if letter == 'O' or letter == 'Q':
            print(letter + 'u' + suffix)
        else:
            print(letter + suffix)

# ex-02

def count(word, letter):
    """
    This function takes 2 arguments: word and letter. This function computes how many times the inputted letter will show up in the inputted word.
    """

    count = 0
    for i in word:
        if i == letter:
            count += 1
    print(count)

# ex-03

# import antigravity

def string_methods():
    user_response = input("Do you wanna read the string methods documentation? >>> ")
    if user_response == 'Yes' or 'yes' or 'yeah' or 'Yeah':
        import webbrowser
        url = 'https://docs.python.org/3/library/stdtypes.html#string-methods'
        webbrowser.open(url)
    else:
        print('Come back when you are lost!')
# Read the documentation of the string methods at https://docs.python.org/3/library/stdtypes.html#string-methods

# ex-04



