'''
This module is a collection of methods 
for generating data of non-existent persons.

CREATED BY GENE GREEN (c)
2023
realgenegreen@gmail.com
'''
import random
from data import M_NAMES, F_NAMES, SURNAMES, M_PROFESSIONS, F_PROFESSIONS

def m_name():
    '''Male names'''
    return random.choice(M_NAMES.split())

def f_name():
    '''Female names'''
    return random.choice(F_NAMES.split())

def surname():
    '''Surnames'''
    return random.choice(SURNAMES.split())

def m_prof():
    '''Professions common among mens'''
    return random.choice(M_PROFESSIONS.split())

def f_prof():
    '''Professions common among women'''
    return random.choice(F_PROFESSIONS.split())
