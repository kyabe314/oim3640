from exercises_11 import uses_only

def has_o(word):
    """
    
    """
    return 'o' in word

def todays_spelling_bee():
    """
    
    """
    f = open('data/words.txt')
    for line in f:
        line = line.strip()
        if len(line) >= 4:
            test_1 = has_o(line)
            if test_1 is True:
                test_2 = uses_only(line, 'ogwnhpi')
                if test_2 is True:
                    print(line)
            

todays_spelling_bee()