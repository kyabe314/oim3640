# ex-02.02

def anagram():
    """
    
    """
    d = dict()
    f = open('data/words.txt')
    for line in f:
        line = line.strip()
        print(line)
        name1 = line # preserve the original string
        d[name1] = []
        line = sorted(line)
        for line2 in f:
            line2 = line2.strip()
            # print(line2)
            name2 = line2 # preserve the original string
            line2 = sorted(line2)
            # print(line2)
            if line == line2:
                d[name1].value().append(name2)
                
    return d

# ex-02.03
# order the values in from the longest to shortest
def anagram_longesttoshortest():
    """
    
    """
    d = dict()
    f = open('data/words.txt')
    for line in f:
        line = line.strip()
        print(line)
        name1 = line # preserve the original string
        d[name1] = []
        line = sorted(line)
        for line2 in f:
            line2 = line2.strip()
            # print(line2)
            name2 = line2 # preserve the original string
            line2 = sorted(line2)
            # print(line2)
            if line == line2:
                d[name1].value().append(name2)
    for k, v in d:
        for e in v:
            counter = 0
            lst = list()
            if counter == 0:
                counter =+ 1
                lst.append(e)
            else:
                if len(e) > len(v[k - 1]):
                    lst[k - 1] = e
                    lst[k] = v[k - 1]
                else:
                    lst.append(e)


                
    return d
        
def main():
    print(anagram())

if __name__ == '__main__':
    main()
        
        




