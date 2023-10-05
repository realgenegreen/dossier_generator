'''
This module is a collection of methods 
for generating data of non-existent persons.

CREATED BY GENE GREEN (c)
2023
realgenegreen@gmail.com
'''

import random

def m_name():
    with open('data/m_names.txt', 'r') as file:
        output = file.read().split()

        return random.choice(output)

def f_name():
    with open('data/f_names.txt', 'r') as file:
        output = file.read().split()

        return random.choice(output)

def surname():
    with open ('data/surnames.txt', 'r') as file:
        output = file.read().split()

        return random.choice(output)

def password():
    with open ('data/pwdsym.txt', 'r') as file:
        output = file.read().split()

        pwd =''
        cnt = 0
        for sym in output:
            if cnt >= 8:
                break
            pwd += random.choice(output)
            cnt += 1

        return pwd

def m_prof():
    with open('data/m_professions.txt', 'r') as file:
        output = file.read().split()

        return random.choice(output)

def f_prof():
    with open('data/f_professions.txt', 'r') as file:
        output = file.read().split()

        return random.choice(output)
