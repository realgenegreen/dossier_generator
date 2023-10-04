#
# CREATED BY GENE GREEN (c)
# 2023
# realgenegreen@gmail.com
#

import random
from credentials import surname

def _coin():
    coin = random.randint(0,1)
    return (coin)

def _coin1():
    coin = random.randint(0,2)
    return (coin)

def _coin2():
    coin = random.randint(0,3)
    return (coin)

def root():
    if _coin() == 0:
        with open('data/surnames.txt', 'r') as sfile:
            output1 = sfile.read().split()

            return(random.choice(output1))
    else:
        with open('data/town_rtwd.txt', 'r') as tfile:
            output2 = tfile.read().split()

            return(random.choice(output2))
        
def towns():
    if _coin() == 0:
        with open('data/town_pfix.txt', 'r') as pfile:
            output1 = pfile.read().split()

            pfix = (random.choice(output1))

            return (root()+pfix)
    else:
        with open('data/town_dblw.txt', 'r') as dfile:
            output2 = dfile.read().split()

            pfix = (random.choice(output2))

            return (root()+' '+pfix)

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

    if not _coin2() == 0:
        type_list = ['Ave', 'Blwd', 'Dr', 'Rd', 'St']
        st_type = (random.choice(type_list))
    else:
        type_list = ['Cir', 'Ct', 'Ln', 'Pkwy', 'Pl', 'Hwy', 'Fwy', 'Bldg']
        st_type = (random.choice(type_list))

    if _coin() == 0:
        st_name = root()
    if st_type in ['Ave', 'St'] and _coin() == 1:
        st_name = _st_num()
    else:
        with open('data/st_rtwd.txt', 'r') as file:
            output = file.read().split()
            st_name = (random.choice(output))

    return (st_name+' '+st_type)

def address(twn):

    return (str(random.randrange(1,700,1))+' '+street()+', '+twn+' '+str(random.randrange(10000,99999,1)))

def education():

    if _coin() == 0:
        mid_univ = ''
    else:
        mid_univ = (random.choice(['State ', 'Central ', 'Technical ', 'Research ']))

    def _naming():
        if _coin() == 0:
            naming = towns()
        else:
            naming = surname()
        return(naming)

    if _coin1() == 0:
        int_univ = f'{_naming()} '
        end1_univ = ''
    elif _coin1() == 1:
        int_univ = ''
        end1_univ = f'of {_naming()}'
    else:
        int_univ = f'{_naming()} '
        end1_univ = f'of {_naming()}'

    if not end1_univ == '' and _coin() == 0:
        end_univ = str('of '+(random.choice(['Health ', 'Technology ', 'Art ', 'Arts ', 'Justice ', 'Medicine ', 'Science ', 'Culture '])))
    else:
        end_univ = end1_univ

    if not _coin2() == 0:
        univ = (random.choice(['University', 'Institute', 'College', 'Academy']))
    else:
        univ = None
    
    if univ == None:
        return (None)
    else:
        return f'{int_univ}{mid_univ}{univ} {end_univ}'
