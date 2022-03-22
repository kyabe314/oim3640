# API = search equivalent for humans
# right click to .gitignore

# tupel is an immutable list
# t = "a", "b", "c" -> tuple

# t = 'a', 'b', 'c'
# print(type(t))

# unpacking 
# root1, root2 = tuple -> unpack elements in tuple and assign each a variable name

# Tuple assignment (you just need to do this to swap!)
# a, b = b, a

# string and list
name = 'raphael'
lst = list(name)
# print(lst)

name = 'raphael prem'
lst = name.split()
# print(lst)

string = ' '.join(lst)
# print(string)

from collections import Counter

counter = Counter(name)
# print(counter)

# string and set
s = set(name)
print(s)

# list and dictionary

# We can use a tuple as a key, not a list

# f = open('data/words.txt')
# print(type(f))

# 1. read words.txt into a list of words
# 2. sort one word, convert the word to a sorted tuple/string
# 3. Create a dictionary, key is the sorted tuple/string, and value is a list of anagram words
# 4. Create a new list, by getting the values of dict only - we only want the lists that have more tahn one word, and return the list
# 5. print the list
# 5. create another dict like this:
# {2:[['spot', 'pots'],['ab', 'ba']], 7:}
