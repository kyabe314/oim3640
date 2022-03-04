# Dictionary

name = ['Lily', 'Smit', 'Mezue']
score = [95, 75, 85]

# Dictionary is mapping

grades = dict() # or {}

grades['Smit'] = 75
grades = {'Smit':75, 'Lily':95, 'Mezue':85}
# print(grades)

# print('Lily' in grades)
# print(grades.keys())

grades.values()

def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1

    return d



word = 'bookkeeper'
h = histogram(word)
print(h)