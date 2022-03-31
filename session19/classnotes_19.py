# What are some things you have automated, using Python? (on Reddit)
# How automation works (on Reddit)
# batch script -> a set of Windows command
# Windows task scheduler
# A Markov-Chain Twitter bot trained on Elon Musk Tweets and Childrens Books

# 3 errors -> syntax, runtime, and semantics errors

# I/O Programming

# Q: Why is I/O so important?

# fout = open('data/dylan.txt', 'a')

# line1 = "How many roads must a man walk down\n"
# fout.write(line1)

# line2 = "Before you call him a man?\n"
# fout.write(line2)

# fout.close()

import os


with open('data/dylan.txt', 'w') as fout:
    line1 = "How many roads must a man walk down\n"
    fout.write(line1)
    line2 = "Before you call him a man?\n"
    fout.write(line2)

name = "Kotaro"

for i, letter in enumerate(name):
    print(i, letter)



cwd = os.getcwd()
print(cwd)

def walk(dirname):
    """Prints the names of all files in 
    dirname and its subdirectories.

    dirname: string name of directory
    """
    for name in os.listdir(dirname):
        path = os.path.join(dirname, name)

        if os.path.isfile(path):
            print(path)
        else:
            walk(path)

# control + . -> possible actions
# walk(os.getcwd())

try:
    f = open('data/data.txt')
    
except Exception as e:
    print(e)

print('Hello, World!')

# CSV writer Python
# https://docs.python.org/3/library/csv.html

# sqlite3 -> small application
# SQL -> Structure Query Language

import pickle
d = {'a':1, 'b':2, 'c':3}

# with open('data/d.txt', 'w') as f:
#     f.write(d)

with open('data/d.pickle', 'wb') as p:
    pickle.dump(d, p)

import pickle
with open('data/d.pickle', 'rb') as f:
    t2 = pickle.load(f)

print(t2)
print(type(t2))