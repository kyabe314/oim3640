def nested_sum(t):
    """Computes the total of all numbers in a list of lists.

    t: list of list of numbers

    returns: number

    Expected output:
    >>> t = [[1, 2], [3], [4, 5, 6]]
    >>> nested_sum(t)
    21
    """

    # Create a variable in which the function stores the sum of all the numbers
    result = 0

    # 'for' loop for the components in the list
    for lst in t:

        # for loop for the componenst in the nested list
        for i in lst:

            #Add the component to the counter variable
            result += i

    return result


def cumsum(t):
    """Computes the cumulative sum of the numbers in t.

    t: list of numbers

    returns: list of numbers

    Expected output:
    >>> t = [1, 2, 3]
    >>> cumsum(t)
    [1, 3, 6]
    """
    
    new_t = []
    for i in t:
        if i == t[0]:
            prev_i = i
            new_t.append(i)
        else:
            new_t.append(i + prev_i)
            prev_i = i + prev_i
    
    return new_t


def middle(t):
    """Returns all but the first and last elements of t.

    t: list

    returns: new list

    Expected output:
    >>> t = [1, 2, 3, 4]
    >>> middle(t)
    [2, 3]
    """

    new_list = t[1:-1]
    return new_list


def chop(t):
    """Removes the first and last elements of t.

    t: list

    returns: None

    Expected output:
    >>> t = [1, 2, 3, 4]
    >>> chop(t)
    >>> t
    [2, 3]
    """
    t.remove(t[-1])
    t.remove(t[-1])
    return


def is_sorted(t):
    """Checks whether a list is sorted.

    t: list

    returns: boolean

    Expected output:
    >>> is_sorted([1, 2, 2])
    True
    >>> is_sorted(['b', 'a'])
    False
    """
    new_t = t[:]
    new_t.sort()
    # print(new_t)
    return t == new_t


def is_anagram(word1, word2):
    """Checks whether two words are anagrams

    Two words are anagrams if you can rearrange the letters from one to
    spell the other.

    word1: string or list
    word2: string or list

    returns: boolean

    Expected output:
    >>> is_anagram('stop', 'pots')
    True
    >>> is_anagram('different', 'letters')
    False
    >>> is_anagram([1, 2, 2], [2, 1, 2])
    True
    """
    # Create a list for each word
    list_1 = []
    list_2 = []
    
    # Extend the string into each letter. Unaffected if the object is integer/float
    list_1.extend(word1)
    list_2.extend(word2)
    # print(list_1)
    # print(list_2)

    # Sort each list in order to aligh each component for anagram examination
    list_1.sort()
    list_2.sort()

    return list_1 == list_2


def has_duplicates(s):
    """Returns True if any element appears more than once in a sequence.

    s: string or list

    returns: bool

    output:
    >>> print(has_duplicates('cba'))
    False
    >>> print(has_duplicates('abba'))
    True
    """
    s_list = []
    s_list.extend(s)
    s_list.sort()
    # print(s_list)
    for element in s_list:
        # print(element)
        if element == s_list[0]:
            prev_element = element
        else:
            if prev_element == element:
                return True
        prev_element = element
    return False


def has_adjacent_duplicates(s):
    """Returns True if there are two same adjacent elements.

    s: string or list

    returns: bool

    output:
    >>> print(has_adjacent_duplicates('cba'))
    False
    >>> print(has_adjacent_duplicates('abca'))
    False
    >>> print(has_adjacent_duplicates('abbc'))
    True
    """
    
    list_s = []
    list_s.extend(s)
    for element in s:
        if list_s.index(element) + 1 > len(list_s) - 1:
            break
        elif element == list_s[list_s.index(element) + 1]:
            return True
    return False


def main():
    # t = [[1, 2], [3], [4, 5, 6]]
    # print(nested_sum(t))

    # t = [1, 2, 3]
    # print(cumsum(t))

    # t = [1, 2, 3, 4]
    # print(middle(t))
    # chop(t)
    # print(t)

    # print(is_sorted([1, 2, 2]))
    # print(is_sorted(['b', 'a']))

    # print(is_anagram('stop', 'pots'))
    # print(is_anagram('different', 'letters'))
    # print(is_anagram([1, 2, 2], [2, 1, 2]))

    # print(has_duplicates('cba'))
    # print(has_duplicates('abba'))

    print(has_adjacent_duplicates('cba'))
    print(has_adjacent_duplicates('abca'))
    print(has_adjacent_duplicates('abbc'))


if __name__ == "__main__":
    main()
