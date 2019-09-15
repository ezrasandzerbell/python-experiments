import random

eyes = ["brown", "blue", "green"]
noses = ["big", "pointy", "tiny"]
mouths = ["broad", "thin", "juicy"]
i = 1

eye = random.choice(eyes)
nose = random.choice(noses)
mouth = random.choice(mouths)
print("They have " + eye + " eyes with a " + nose + " nose and a " + mouth + " mouth." )

while i < 6:
    answer = input("Want to generate another emoticon? ")
    if answer == 'yes':
        eye = random.choice(eyes)
        nose = random.choice(noses)
        mouth = random.choice(mouths)
        print("They have " + eye + " eyes with a " + nose + " nose and a " + mouth + " mouth." )
    elif answer == "no":
        i = 6
        print("alright, later!")
    else:
        answer2 = input("Yes or no, hmm?")
        if answer2 == "yes":
            eye = random.choice(eyes)
            nose = random.choice(noses)
            mouth = random.choice(mouths)
            print("They have " + eye + " eyes with a " + nose + " nose and a " + mouth + " mouth." )
        else:
            i = 6
            print("alright, later!")
    i += 1
