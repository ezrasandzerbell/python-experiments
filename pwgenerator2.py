import random

alphabetBank = ['a', 'b', 'c', 'd', 'e']
numeralBank = ['1', '2', '3', '4', '5']
punctuationBank = ['!', '.', ',', '?']
password = []
iAlpha = 1
iNumera = 1
iPunctua = 1

alphaLength = int(input("How many alphabet characters would you like the password to have?"))


while iAlpha <= alphaLength:
    password.append(random.choice(alphabetBank))
    iAlpha+=1

numeraLength = int(input("How many numerals would you like the password to have?"))

while iNumera <= numeraLength:
    password.append(random.choice(numeralBank))
    iNumera+=1

punctuaLength = int(input("How many punctuation marks would you like the password to have?"))

while iPunctua <= punctuaLength:
    password.append(random.choice(punctuationBank))
    iPunctua+=1

random.shuffle(password)
pw = ''.join(password)

print(pw)
