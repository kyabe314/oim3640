def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d

h = histogram('Bookkeeper')
# print(h)

number_of_e = h.get('e', 0)
number_of_c = h.get('c', 0)
# print(number_of_e)
# print(number_of_c)

def print_hist(h):
    for c in h:
        print(c, h[c])

# In the order that the key was appended to dictionary
h = histogram('Massachusetts')
# print_hist(h)

# In the alphabetical order, upper case to lower case
# for key in sorted(h):
#     print(key, h[key])

# reverse lookup
def reverse_lookup(d, v):
    for k in d:
        if d[k] == v:
            return k
    raise LookupError('The value does not appear in the dictionary')

h = histogram('Massachusetts')
key = reverse_lookup(h, 2)
# print(key)

def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
    return inverse

hist = histogram('parrot')
# print(hist)

inverse = invert_dict(hist)
# print(inverse)

# lists are unhashable
# t = [1, 2, 3]
# d = dict()
# d[t] = 'oops'

known = {0:0, 1:1}

def fibonacci(n):
    if n in known:
        return known[n]

    res = fibonacci(n-1) + fibonacci(n-2)
    known[n] = res
    return res

for i in range(10):
    print(fibonacci(i), end=', ')
