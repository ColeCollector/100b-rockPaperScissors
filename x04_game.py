#!python3

"""
Create a full rock paper scissors game
You can incorporate the other files in this project to help you
"""

from x01_player import *
from x02_computer import *
from x03_winner import *

if __name__ == "__main__":
  computer = computerChoice()
  player = playerChoice()
  winner = playerWins(computer,player)
  
  if winner == -1:
    if computer == 0:
      print("You lost, I picked rock")

    elif computer == 1:
      print("You lost, I picked paper")

    elif computer == 2:
      print("You lost, I picked scissors")

  if winner == 1:
    if computer == 0:
      print("You Won, I picked rock")

    elif computer == 1:
      print("You Won, I picked paper")

    elif computer == 2:
      print("You Won, I picked scissors")
  
  if winner == 0:
    if computer == 0:
      print("It was a draw, we both picked rock")

    elif computer == 1:
      print("It was a draw, we both picked paper")

    elif computer == 2:
      print("It was a draw, we both picked scissors")



