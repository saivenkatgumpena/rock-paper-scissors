import random

choices = ["rock", "paper", "scissors"]

print("Welcome to Rock, Paper, Scissors!")
print("Type 'bye' anytime to stop playing.\n")

while True:
    user = input("Choose rock, paper or scissors: ").lower()
    
    if user == "bye":
        print("Thanks for playing! Goodbye! 👋")
        break

    if user not in choices:
        print("Invalid choice. Try again.")
        continue

    computer = random.choice(choices)

    print("You chose:", user)
    print("Computer chose:", computer)

    if user == computer:
        print("It's a tie!")
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        print("You win!")
    else:
        print("Computer wins!")

    print() 
