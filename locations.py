"""
This module is a collection of methods 
for generating non-existent geographic locations.

CREATED BY GENE GREEN (c)
2023
realgenegreen@gmail.com
"""

import random
from data import SURNAMES, TOWN_RTWD, TOWN_DBLW, TOWN_PFIX, ST_RTWDS
from __init__ import _coin, _dice

def _root():
    if _coin() == 0:
        return random.choice(SURNAMES.split())
    return random.choice(TOWN_RTWD.split())

def towns():
    """Town name generator"""
    if _coin() == 0:
        pfix = random.choice(TOWN_PFIX.split())
        return _root()+pfix
    else:
        pfix = random.choice(TOWN_DBLW.split())
        return _root()+' '+pfix

def street():
    """Street name generator"""
    def _st_num():
        num = str(random.randrange(1, 200, 1))
        ind = num[-1]
        if ind == '1':
            pfx = 'st'
        elif ind == '2':
            pfx = 'nd'
        elif ind == '3':
            pfx = 'rd'
        else:
            pfx = 'th'
        return str(num+pfx)

    if not _dice() == 0:
        type_list = ['Ave', 'Blwd', 'Dr', 'Rd', 'St']
        st_type = random.choice(type_list)
    else:
        type_list = ['Cir', 'Ct', 'Ln', 'Pkwy', 'Pl', 'Hwy', 'Fwy', 'Bldg']
        st_type = random.choice(type_list)

    if _coin() == 0:
        st_name = _root()
    if st_type in ['Ave', 'St'] and _coin() == 1:
        st_name = _st_num()
    else:
        st_name = random.choice(ST_RTWDS.split())
    return st_name+' '+st_type

def address(twn):
    """Address string generator"""
    num_1 = random.randrange(1,700,1)
    num_2 = random.randrange(10000,99999,1)
    return f'{num_1} {street()}, {twn} {num_2}'

def education():
    """Education info generator"""
    if _coin() == 0:
        mid_univ = ''
    else:
        mid_univ = random.choice(['State ', 'Central ', 'Technical ', 'Research '])

    def _naming():
        if _coin() == 0:
            naming = towns()
        else:
            naming = random.choice(SURNAMES.split())
        return naming

    if _dice() == 0:
        int_univ = f'{_naming()} '
        end1_univ = f'of {_naming()}'
    elif _dice() == 1:
        int_univ = ''
        end1_univ = f'of {_naming()}'
    else:
        int_univ = f'{_naming()} '
        end1_univ = ''

    if end1_univ != '' and _coin() == 0:
        end_univ = str('of '+(random.choice(['Health ', 'Technology ', 'Art ',
                                             'Arts ', 'Justice ', 'Medicine ', 
                                             'Science ', 'Culture '])))
    else:
        end_univ = end1_univ

    if not _dice() == 0:
        univ = random.choice(['University', 'Institute', 'College', 'Academy'])
    else:
        univ = None

    if univ is None:
        return None

    return f'{int_univ}{mid_univ}{univ} {end_univ}'
