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
    """
    
    """
    user_response = input(
        "Do you wanna read the string methods documentation? >>> ")
    if user_response == 'Yes':
        import webbrowser
        url = 'https://docs.python.org/3/library/stdtypes.html#string-methods'
        webbrowser.open(url)
    else:
        print('Come back when you are lost!')
# Read the documentation of the string methods at https://docs.python.org/3/library/stdtypes.html#string-methods

# ex-04

# any_lowercase1(s) checks every single letter in the string, and returns 'True' in an instant the function finds the first lowercase letter. This function is correct in this context.

# any_lowercase2(s) does not refer to letters in a given string, but rather to one partcular string, 'c'. The function checks if 'c' is lowercase, and returns a string 'True,' and 'False' otherwise. Since 'c' is a lowercase, the function will return a string 'True,' regardless of the value in "s". This function is wrong in this context.

# any_lowercase3(s) stores 'True' in 'flag" variable if the string contains lowercase, and 'False' otherwise. The function returns the boolean value of the last character stored in the variable. This function is wrong in this context.

# any_lowercase4(s) compares 'False' value stored in 'flag' variable and compares it to boolean value returned from .islower() function using 'or' boolean expression. Since False or False == False and False or True == True, the function practically stores whatever value is obtained from .islower() into flag, which gets updated step by step. As long as at least one lowercase is contained, flag value will remain True, which works as a check for lowercase in a string. This function is correct in this context.

# any_lowercase5(s) returns False if there is even a single upper case letter combined. This function returns True if all the letters are lowercases. This function is wrong in this context.


# ex-05

# Unicode range for uppercase: 65-90
# Unicode range for lowercase: 97-122

def rotate_word(word, rotation):
    """
    
    """
    google_parent = 26
    ceaser_word = ''
    if rotation >= 0:
        rotation = rotation % google_parent
    else:
        abs_rotation = abs(rotation)
        rotation = -(abs_rotation % google_parent)
        
    for letter in word:
        if not 65 <= ord(letter) <= 90 and not 97 <= ord(letter) <= 122:
            ceaser_word += letter
        if letter.islower():
            base = ord(letter) - 97
            ceaser = (base + rotation) % google_parent
            if ceaser < 0:
                letter_ord = 123 + ceaser
            elif ceaser >= 0:
                letter_ord = 97 + ceaser
            # print(letter_ord)
            letter = chr(letter_ord)
            ceaser_word += letter

        elif letter.isupper():
            base = ord(letter) - 65
            ceaser = (base + rotation) % google_parent
            if ceaser < 0:
                letter_ord = 91 + ceaser
            elif ceaser >= 0:
                letter_ord = 65 + ceaser
            letter = chr(letter_ord)
            ceaser_word += letter

    return ceaser_word
                
def input_rotate_word():
    word = input('Type in a word you want to convert using Ceaser cypher! >>> ')
    rotation = int(input('Type in the number of rotation >>> '))
    print(rotate_word(word, rotation))

# Python challenge 01

# input_rotate_word()

def main():
    ducklings()
    count('New England Patriots', 'a')
    # string_methods()

    challenge_1 = 'g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr\'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.'

    challenge_2 = 'http://www.pythonchallenge.com/pc/def/map.html'

    print(rotate_word(challenge_1, 2))
    print(rotate_word(challenge_2, 2))

    #input_rotate_word()


if __name__ == '__main__':
    # main()
    pass
