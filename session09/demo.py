team = 'New England Patriots'
# print(team[0:11])
# print(team[12:20])
# print(team[4:3])
# print(team[:])
# print(team[::3])

# team[12:20] = 'Seahawks'

new_team = team[:12] + 'Seahawks'
# print(new_team)

# print(team)

def find(word, letter):
    index = 0
    while index < len(word):
        if word[index] == letter:
            return index 
        index += 1
    return -1 # when "letter" is not found

# print(find(team, 'A'))

# count how many of a particular letter is in a string
word = 'New England Patriots'
count = 0
for letter in word:
    if letter == 'a':
        count += 1
# print(count)

new_team_1 = team.upper()
# print(new_team_1)

index = team.find('a', 10)
print(index)

# print('a' in team)

name = 'bob'
print(name.find('b', 1, 2))