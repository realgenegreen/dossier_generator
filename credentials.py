import random

def m_name():
    with open('m_names.txt', 'r') as mfile:
        output1 = mfile.read().split()

        return(random.choice(output1))
    
def f_name():
    with open('f_names.txt', 'r') as ffile:
        output1 = ffile.read().split()

        return(random.choice(output1))
    
def surname():
    with open ('surnames.txt', 'r') as sfile:
        output2 = sfile.read().split()

        return(random.choice(output2))

def password():
    with open ('pwdsym.txt', 'r') as pfile:
        output3 = pfile.read().split()

        pwd =''
        cnt = 0
        for sym in output3:
            if cnt >= 8:
                break
            pwd += random.choice(output3)
            cnt += 1

        return(pwd)

def m_prof():
    with open('m_professions.txt', 'r') as file:
        output = file.read().split()

        return(random.choice(output))
    
def f_prof():
    with open('f_professions.txt', 'r') as file:
        output = file.read().split()

        return(random.choice(output))