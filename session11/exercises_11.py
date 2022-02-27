import os
import string
from itertools import combinations, count

# print(os.getcwd())

# ex-01.01

def long_words():
    """
    print words that contain more than 20 letters
    """

    f = open('data/words.txt')

    for line in f:
        line = line.strip()
        if len(line) > 20:
            print(line, len(line))

# ex-01.01

def has_no_e(word):
    """
    Take a string argument in "word" and check if the word contains no "e." Returns True if it does not and False it does.
    """
    # print(word)
    for letter in word.lower():
        # print(letter)
        if letter == 'e':
            return False
    return True

def has_no_e_alt(word):
    """
    An alternative approach to "has_no_e()" function.
    """
    return 'e' not in word.lower()

def no_e_words():
    """
    Print words that do not contain "e" and calculate the percentage of it.
    """
    f = open('data/words.txt')
    count = 0
    no_e_count = 0
    for line in f:
        count += 1
        line = line.strip()
        has_no_e_alt(line)
        if has_no_e_alt(line) == True:
            no_e_count += 1
            # Uncomment the following line for printing
            # print(line)
    
    print(no_e_count, count, str(round((no_e_count/count)*100, 2)) + '%')

# ex-01.03

def avoids(word, forbidden_letters):
    """
    Search for letters from forbidden_letters argument in word argument and returns False if the word contains any of the words and True if it does not.
    """
    for letter in word.lower():
        # print(letter)
        if letter in forbidden_letters:
            return False
    return True

def avoids_modified():
    """
    Prompt a user to enter a set of forbidden letters and search for words which do not contain them.
    """
    user_input = input('Enter a string of letters that you do not want in given words >>> ')

    count_without_forbidden = 0
    f = open('data/words.txt')

    for line in f:
        line = line.strip()
        test = avoids(line, user_input)
        if test == True:
            count_without_forbidden += 1
        
    
    return count_without_forbidden

def avoids_modified2(forbidden_letters):
    """
    Prompt a user to enter a set of forbidden letters and search for words which do not contain them.
    """

    count_without_forbidden = 0
    f = open('data/words.txt')

    for line in f:
        line = line.strip()
        test = avoids(line, forbidden_letters)
        if test == True:
            count_without_forbidden += 1
        
    
    return count_without_forbidden

def exhaustive_search_of_5_forbidden_letters():
    """
    Extract every 5-letter combination of 26 alphabet letters and test them on the dictionary to see which combination returns the least number of words
    """
    
    # The following code took so long to run that I did not reach a definitive answer
    #

    # Credit:  https://www.kite.com/python/answers/how-to-make-a-list-of-the-alphabet-in-python for creating a list of the alphabets
    # Credit: https://stackoverflow.com/questions/104420/how-to-generate-all-permutations-of-a-list for creating a list of permutations
    # Credit: https://stackoverflow.com/questions/12453580/how-to-concatenate-items-in-a-list-to-a-single-string for concatenating elements in a list

    alphabet_string = string.ascii_lowercase
    # print(alphabet_string)
    possibilities = list(combinations(alphabet_string, 5))
    # print(possibilities)
    # count = 0
    # for _ in possiblities:
    #     count += 1
    # print(count)
    
    smallest_combo = ''
    smallest_combo_count = float('inf')
    
    count_possibilities = 0
    for _ in possibilities:
        count_possibilities += 1
    
    # print(count_possibilities)

    for i in range(count_possibilities):
        each_count = 0
        possibilities[i] = ''.join(list(possibilities[i]))
        # print(possibilities[0])

        test = avoids_modified2(possibilities[i])

        if test < smallest_combo_count:
            smallest_combo_count = each_count
            smallest_combo = possibilities[i]
        # print('counting?')
    return smallest_combo, smallest_combo_count

# My guess is 'aeiou' with 107 words left

# ex-01.04

def uses_only(word, criteria):
        for letter in word:
            if letter not in criteria:
                return False
        return True

def planets():
    """
    Faulty
    """
    f = open('data/words.txt')
    for line in f:
        line = line.strip()
        test = uses_only(line, 'planets')
        if test == True:
            print(line)

# ex-01.05

def uses_all(word, criteria):
    """
    """
    # reverse the order
    for letter in criteria:
        if letter not in word:
            return False
    return True

# ex-01.06

def is_abecedarian(word):
    """
    
    """
    one_letter_before = word[0]
    for letter in word:
        if ord(letter) < ord(one_letter_before):
            return False
        else:
            one_letter_before = letter
    return True


def main():
    # long_words()
    # print(has_no_e('hello'))
    # print(has_no_e_alt('hello'))
    # no_e_words()
    # print(avoids('communication', 'e'))
    # print(avoids_modified())
    # print(exhaustive_search_of_5_forbidden_letters())
    # print(exhaustive_search_of_5_forbidden_letters())
    # print(uses_only('communication','planets'))
    # planets()
    # print(uses_all('communication', 'aeiou'))
    print(is_abecedarian('abcde'))

    pass

if __name__ == '__main__':
    main()