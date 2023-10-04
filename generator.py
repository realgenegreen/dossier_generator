#
# CREATED BY GENE GREEN (c)
# 2023
# realgenegreen@gmail.com
#

import random
from credentials import f_name, m_name, surname, m_prof, f_prof
from locations import towns, address, education

def coin():
    coin_v = random.randint(0,1)
    return coin_v

def dice():
    dice_v = random.randint(0,3)
    return dice_v

def badrate():
    rate = random.randint(0,15)
    return rate

#GEN
if not coin() == 1:
    name = f_name()
    gen = 'Female'
else:
    name = m_name()
    gen = 'Male'

pid = random.randrange(0000000,99999999,1)
date = str(random.randrange(1,30,1))+' '+str(random.choice(['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']))+' '+str(random.randrange(1955,1999,1))
true_driver = ''.join(random.choices(['A','B','C','D','E','F','G','H','J','I','K','L','M','N','O','P','R','S','T','Q','U','V','W','X','Y','Z'],k=2))+' '+str(random.randrange(00000,99999,1))+' '+str(random.choice(['A','B','C','D']))

#DRIVER
if dice() == 0:
    driver = None
else:
    driver = true_driver

#OCCUPATION
if dice() == 0:
    occu = 'Unemployed'
elif not gen == 'Male':
    occu = f_prof()
else:
    occu = m_prof()

#SOCIAL
edu = education()

if edu is None:
    occu = (random.choice([
            'Attendant', 'Dustman', 'Barber', 'Driver', 
            'Unemployed','Unemployed','Unemployed']))

if occu == 'Unemployed' and edu is None:
    rmin = 15
    rmax = 30
elif occu == 'Unemployed' or edu is None:
    rmin = 25
    rmax = 45
else:
    rmin = 45
    rmax = 100

socr = random.randint(rmin,rmax)

if socr >= 70:
    rcom = 'Worthy'
elif socr <= 35:
    rcom = 'Unreliable'
else:
    rcom = 'Unremarkable'

#TOWN
birthtown = towns()
if coin() == 0:
    town = towns()
else:
    town = birthtown

#==============PRINT BLOCK================
print('\n'+
    'Name:',name,surname(),'\n'+
    'Gender:',gen,'\n'+
    'ID:',pid,'\n'+
    'Date of Birth:',date,'\n'+
    'Birthplace:',birthtown,'\n'+
    'Location Address:',address(town),'\n'+
    'Driver License:',driver,'\n'+
    'Occupation:',occu,'\n'+
    'Education:',edu,'\n'+
    'Social Rating:',socr,rcom,'\n'
    )
