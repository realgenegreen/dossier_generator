import random
from credentials import f_name, m_name, surname, password

n1 = f_name
n2 = m_name
name = ''
coin = random.randint(0,1)

if not coin == 1:
    name = f_name
else:
    name = m_name

print(f_name)

# print(
#     'Name:',f_name,'\t'+
#     'Surname:',surname,'\t'
#     )