# ex-01

def histogram(s):
    d = dict()
    s = s.replace(' ','')
    for c in s:
        d[c] = d.get(c, 0) + 1

    return d

# ex-02
# play with fibonacci_counted.py 

# ex-03
# Another global variable that is used in fibonacci_counted.py is 'number_fib_calls'
# The difference between 'known' and 'number_fib_calls' is that 'known' is defined outside any function whereas 'number_fib_calls' is specified as global within a function so that it can work as a counter everytime the function is repeated

# ex-04

def librarian():
    f = open('data/words.txt')
    d = dict()
    for line in f:
        line = line.strip()
        d[line] = d.get(line, 0) + 1
    return d

def has_duplicates(list_of_words):
    for word in list_of_words:
        # print(word)
        test = librarian().get(word, 0)
        print(test)
        if test > 1:
            return True
    return False


def main():
    h = histogram('A Thousand Miles')
    # print(h)
    librarian()
    # print(librarian())
    index_word = 'hello'
    # print(index_word.lower() in librarian())
    list_of_words = ['hkjbs', 'hello']
    print(has_duplicates(list_of_words))

if __name__ == '__main__':
    main()
