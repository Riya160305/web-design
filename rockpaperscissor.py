import random
print("Rock" , "Paper" , "Scissors Game")
options = ["rock" , "paper" , "scissors"]
user = input("Enter your choice : ").lower()
computer = random.choice(options)
print("computer : " , computer)
if user == computer:
    print("it is a Tie")
elif user == "rock" and computer == "scissors":
    print("You Win")
elif user == "paper" and computer == "rock":
    print("You Win")
elif user == "scissors" and computer == "paper":
    print("You Win")
elif user == "scissors" and computer == "rock":
    print("Computer Win")
elif user == "rock" and computer == "paper":
    print("Computer Win")
elif user == "paper" and computer == "scissors":
    print("Computer Win")
else:
    print("Invalid input")
   