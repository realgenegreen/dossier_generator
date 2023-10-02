import random
from credentials import surname

def _coin():
    coin = random.randint(0,1)
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

def address():
    with open('data/streets.txt', 'r') as file:
            output = file.read().split()

            st = (random.choice(output))

            return (str(random.randrange(1,700,1))+' '+root()+' '+st+', '+str(random.randrange(00000,99999,1)))