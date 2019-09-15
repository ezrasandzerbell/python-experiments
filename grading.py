import random

myScore = random.randint(1, 100)
# rivalScore = random.randint()



answer = input("How would you rate your experience of life so far (1-100): ")

answer = int(answer)

response1 = "You've scored an "
response2 = "You've scored a "

# grammar handling
if (answer >= 90 and answer <= 100):
    print(response1 + "A")
elif (answer >= 80 and answer < 90):
    print(response2 + "B")
elif (answer >= 70 and answer < 80):
    print(response2 + "C")
elif (answer >= 60 and answer < 70):
    print(response2 + "D")
elif (answer < 60 and answer >= 1):
    print(response1 + "F")
else:
    print("Hey, that's not a number between 1-100! Game over.")








# elif answer >= 70
#     print("You've scored a C")
# elif answer >= 60
#     print("You've scored a D")
# else print("You've scored an F")
