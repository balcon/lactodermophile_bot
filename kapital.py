import random
def getRandomSentence():
    with open('daskapital') as f:
        kapital=f.read().replace('\n','').split('. ')
        while True:
            randSentence=random.choice(kapital)
            if len(randSentence)>50:
                break

    return randSentence

if __name__ == "__main__":
    print(getRandomSentence())
