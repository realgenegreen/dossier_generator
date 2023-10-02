import random
from credentials import f_name, m_name, surname, m_prof, f_prof
from locations import towns, address

def coin():
    coin = random.randint(0,1)
    return (coin)

def coin2():
    coin = random.randint(0,3)
    return (coin)

def badrate():
    rate = random.randint(0,25)
    return (rate)

#GEN
if not coin() == 1:
    name = f_name()
    gen = 'Female'
else:
    name = m_name()
    gen = 'Male'

id = random.randrange(0000000,99999999,1)
date = str(random.randrange(1,30,1))+' '+str(random.choice(['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']))+' '+str(random.randrange(1955,1999,1))
true_driver = ''.join(random.choices(['A','B','C','D','E','F','G','H','J','I','K','L','M','N','O','P','R','S','T','Q','U','V','W','X','Y','Z'],k=2))+' '+str(random.randrange(00000,99999,1))+' '+str(random.choice(['A','B','C','D']))

#DRIVER
if not coin() == 1:
    driver = None
else:
    driver = true_driver

#OCCUPATION
if coin2() == 0:
    occu = 'Unemployed'
elif not gen == 'Male':
    occu = f_prof()
else:
    occu = m_prof()

#SOCIAL
if occu == 'Unemployed':
    rmin = 20
    rmax = 50
else:
    rmin = 50
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

print('\n'+
    'Name:',name,surname(),'\n'+
    'Gender:',gen,'\n'+
    'ID:',id,'\n'+
    'Date of Birth:',date,'\n'+
    'Birthplace:',birthtown,'\n'+
    'Location Address:',address(),town,'\n'+
    'Driver License:',driver,'\n'+
    'Occupation:',occu,'\n'+
    'Social Rating:',socr,rcom,'\n'
    )