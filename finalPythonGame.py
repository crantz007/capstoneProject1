#Rock_Paper_Scissors
import random

# input
player = input("Enter your choice (rock/paper/scissors): ")
player = player.lower()
# computing and exceptions
while ( player != "rock" and player != "paper" and player != "scissors"):
   print(player)
   player = input("That choice is not valid. Enter your choice (rock/paper/scissors): ")
   player = player.lower()

cpu = random.randint(0, 2)
if (cpu == 0):
    computer = "rock"
elif (cpu == 1):
    computer = "paper"
elif (cpu == 2):
    computer = "scissors"
else:
    computer = "Error"
if (player == computer):
   print("Draw!")
elif (player == "rock"):
   if (computer == "paper"):
      print("Computer wins!")
   else:
      print("You win!")
elif (player == "paper"):
   if (computer == "rock"):
      print("You win!")
   else:
      print("Computer wins!")
elif (player == "scissors"):
   if (computer == "rock"):
      print("Computer wins!")
   else:
#output
      print("You win!")
print("Your choice: " + player + "\nComputer choice: " + computer + "\nThank you for playing!")
input('press any key to quit:')
