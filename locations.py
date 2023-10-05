'''
This module is a collection of methods 
for generating non-existent geographic locations.

CREATED BY GENE GREEN (c)
2023
realgenegreen@gmail.com
'''

import random
from data import SURNAMES, TOWN_RTWD, TOWN_DBLW, TOWN_PFIX, ST_RTWDS
from . import coin, dice

# def _coin():
#     coin = random.randint(0,1)
#     return coin

# def _coin1():
#     coin = random.randint(0,2)
#     return coin

# def _dice():
#     coin = random.randint(0,3)
#     return coin

def _root():
    if coin() == 0:
        return random.choice(SURNAMES.split())
    return random.choice(TOWN_RTWD.split())

def towns():
    if coin() == 0:
        pfix = random.choice(TOWN_PFIX.split())
        return _root()+pfix
    else:
        pfix = random.choice(TOWN_DBLW.split())
        return _root()+' '+pfix

def street():

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

    if not dice() == 0:
        type_list = ['Ave', 'Blwd', 'Dr', 'Rd', 'St']
        st_type = random.choice(type_list)
    else:
        type_list = ['Cir', 'Ct', 'Ln', 'Pkwy', 'Pl', 'Hwy', 'Fwy', 'Bldg']
        st_type = random.choice(type_list)

    if coin() == 0:
        st_name = _root()
    if st_type in ['Ave', 'St'] and coin() == 1:
        st_name = _st_num()
    else:
        st_name = random.choice(ST_RTWDS.split())
    return st_name+' '+st_type

def address(twn):
    return (str(random.randrange(1,700,1))+' '+street()+', '+twn+' '+str(random.randrange(10000,99999,1)))

def education():

    if coin() == 0:
        mid_univ = ''
    else:
        mid_univ = random.choice(['State ', 'Central ', 'Technical ', 'Research '])

    def _naming():
        if coin() == 0:
            naming = towns()
        else:
            naming = random.choice(SURNAMES.split())
        return naming

    if dice() == 0:
        int_univ = f'{_naming()} '
        end1_univ = f'of {_naming()}'
    elif dice() == 1:
        int_univ = ''
        end1_univ = f'of {_naming()}'
    else:
        int_univ = f'{_naming()} '
        end1_univ = ''

    if end1_univ != '' and coin() == 0:
        end_univ = str('of '+(random.choice(['Health ', 'Technology ', 'Art ', 'Arts ', 'Justice ', 'Medicine ', 'Science ', 'Culture '])))
    else:
        end_univ = end1_univ

    if not dice() == 0:
        univ = random.choice(['University', 'Institute', 'College', 'Academy'])
    else:
        univ = None

    if univ is None:
        return None

    return f'{int_univ}{mid_univ}{univ} {end_univ}'

print(street())