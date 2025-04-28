"""
This is a simple program that generates dossier of non-existent peoples.
This file is main part of it.

CREATED BY GENE GREEN (c)
2023
realgenegreen@gmail.com
"""
import json
import random
from credentials import f_name, m_name, surname, m_prof, f_prof, date, pid, driver_license
from locations import towns, address, education
from __init__ import _coin, _dice

#GEN
if not _coin() == 1:
    name = f_name()
    gen = 'Female'
else:
    name = m_name()
    gen = 'Male'

#OCCUPATION
if _dice() == 0:
    occu = 'Unemployed'
elif not gen == 'Male':
    occu = f_prof()
else:
    occu = m_prof()

#DRIVER
if _dice() != 0 or occu == 'Driver':
    driver = driver_license()
else:
    driver = None

#SOCIAL
edu = education()

if edu is None:
    occu = (random.choice(['Attendant', 'Dustman', 'Barber', 'Driver',
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
if _coin() == 0:
    town = towns()
else:
    town = birthtown

# date = datetime.strptime(date(), "%d %b %Y").strftime("%Y-%m-%d")


def dossier():
    """

    """
    return json.dumps({
        'Name': f'{name} {surname()}',
        'Gender': f'{gen}',
        'ID': pid(),
        'Date of Birth': date(),
        'Birthplace': f'{birthtown}',
        'Location Address': f'{address(town)}',
        'Driver License': f'{driver}',
        'Occupation': f'{occu}',
        'Education': f'{edu}',
        'Social Rating': socr,
        'Social Rating Type': f'{rcom}'
    })

#==============PRINT BLOCK================
# print('\n'+
#     'Name:',name,surname(),'\n'+
#     'Gender:',gen,'\n'+
#     'ID:',pid(),'\n'+
#     'Date of Birth:',date(),'\n'+
#     'Birthplace:',birthtown,'\n'+
#     'Location Address:',address(town),'\n'+
#     'Driver License:',driver,'\n'+
#     'Occupation:',occu,'\n'+
#     'Education:',edu,'\n'+
#     'Social Rating:',socr,rcom,'\n')
