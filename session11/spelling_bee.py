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
            if has_o(line) and uses_only(line, 'ogwnhpi'):
                    print(line)
            

todays_spelling_bee()
