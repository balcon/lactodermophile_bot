import re
import random

def getRhyme():
    f=open('dict')
    dict=f.read().splitlines()
    f.close()

    milkLongEnds=[]
    milkShortEnds=[]
    skinLongEnds=[]
    skinShortEnds=[]

    for word in dict:
        if re.match('\w*очная$',word):
            milkLongEnds.append(word)
        if re.match('\w*ная$',word):
            milkShortEnds.append(word)
        if re.match('\w*енка$',word):
            skinLongEnds.append(word)
        if re.match('\w*ка$',word):
            skinShortEnds.append(word)
    if random.randint(0,1)==0:
        return 'Молочная пенка - '+random.choice(milkShortEnds)+' '+random.choice(skinLongEnds)
    else:
        return 'Пенка молочная - '+random.choice(skinShortEnds)+' '+random.choice(milkLongEnds)

if __name__ == "__main__":
    print(getRhyme())
