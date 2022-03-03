

def contain_bad_words():
    """
    find bad words from a given text file
    """

    # contain at least three words from "covid"
    # contain at least one letter that occurs twice in a row
    # have the same first letter and the last letter

    bad_words_string = 'covid'
    goodwords = []
    f = open('data/random_words.txt')

    for line in f:
        letters = []
        line = line.strip()
        if line[0] == line[-1]:
            letters.extend(line)
            letters.sort()
            for i, letter in line:
                if letter[i] == letter[i - 1]:
                    covid_counter = 0
                    if letter in bad_words_string:
                        covid_counter += 1
                        if covid_counter >= 3:
                            goodwords.append(line)
    
    return goodwords
            

                

        