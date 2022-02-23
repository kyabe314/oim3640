# continue -> done with the current iteration and go to the next loop
# Strings -> ordered collection of other values
# string indices must be integers
# team[len(team)-1]
# team[-1]

prefixes = 'JKLMNOPQ'
suffix = 'ack'

for letter in prefixes:
    if letter == 'O' or letter == 'Q':
        # Other than None, the 'or' will return TRUE
        # print(letter + 'u' + suffix)
        pass
    else:
        # print(letter + suffix)
        pass

# Strings are immutable, cannot change the content directly
