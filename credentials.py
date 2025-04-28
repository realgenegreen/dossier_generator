"""
This module is a collection of methods 
for generating data of non-existent persons.

CREATED BY GENE GREEN (c)
2023
realgenegreen@gmail.com
"""
import random
from data import M_NAMES, F_NAMES, SURNAMES, M_PROFESSIONS, F_PROFESSIONS

def m_name():
    """Male names"""
    return random.choice(M_NAMES.split())

def f_name():
    """Female names"""
    return random.choice(F_NAMES.split())

def surname():
    """Surnames"""
    return random.choice(SURNAMES.split())

def m_prof():
    """Professions common among men"""
    return random.choice(M_PROFESSIONS.split())

def f_prof():
    """Professions common among women"""
    return random.choice(F_PROFESSIONS.split())

def date():
    """Birthday generator"""
    d_d = random.randrange(1,30,1)
    d_m = random.choice(['jan', 'feb', 'mar', 'apr',
                        'may', 'jun', 'jul', 'aug', 
                        'sep', 'oct', 'nov', 'dec'])
    d_y = random.randrange(1955,1999,1)
    return f'{d_d} {d_m} {d_y}'

def pid():
    """ID gen"""
    return random.randrange(0000000,99999999,1)

def driver_license():
    """Driver license gen"""
    li_pfx = ''.join(random.choices(['A','B','C','D','E','F','G',
                             'H','J','I','K','L','M','N',
                             'O','P','R','S','T','Q','U',
                             'V','W','X','Y','Z'],k=2))
    li_num = random.randrange(00000,99999,1)
    li_psx = random.choice(['A','B','C','D'])
    return f'{li_pfx} {li_num} {li_psx}'
