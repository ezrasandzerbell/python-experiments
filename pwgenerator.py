import random

characterBank = ['a', 'b', 'c', 'd', 'e', '1', '2', '3', '4', '5']
password = ['']
i = 1

# collect input on pw char length and convert to integer
pwLength = int(input("How many characters would you like the password to be?"))

# loop through
while i <= pwLength:
    password.append(random.choice(characterBank))
    i+=1

# join array and set to variable
pw = ''.join(password)
print(pw)
