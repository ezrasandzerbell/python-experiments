import random

playAgain = 'yes'
# rps = ['rock', 'paper', 'scissors']
rps = {'rock': ['paper', 'scissors'], 'paper': ['scissors', 'rock'], 'scissors': ['paper', 'rock']}

while playAgain == 'yes':
    choice = input("rock, paper, or scissors? ").lower()
    computerChoice = random.choice(list(rps))
    if choice == computerChoice:
        playAgain = input("It's a tie!\nPlay again? ").lower()
    elif choice == 'rock' and computerChoice == 'scissors':
        playAgain = input("You smashed their scissors!\nPlay again? ").lower()
    elif choice == 'rock' and computerChoice == 'papers':
        playAgain = input("They covered you in paper!\nPlay again? ").lower()
    elif choice == 'paper' and computerChoice == 'scissors':
        playAgain = input("They snipped you to pieces!\nPlay again? ").lower()
    elif choice == 'paper' and computerChoice == 'rock':
        playAgain = input("You covered that rock!\nPlay again? ").lower()
    elif choice == 'scissors' and computerChoice == 'paper':
        playAgain = input("You snipped them up!\nPlay again? ").lower()
    elif choice == 'scissors' and computerChoice == 'rock':
        playAgain = input("They just smashed you!\nPlay again? ").lower()
    else: playAgain = input('you were disqualified for your TERRIBLE SPELLING\nPlay again? ').lower()
