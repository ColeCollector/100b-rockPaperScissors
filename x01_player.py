#! python3

"""
Create a function that asks the player for their choice
The function should return:
  rock     : 0
  paper    : 1
  scissors : 2

```
Sample Run:
Enter your choice:
rock

Output: 0
"""
import random

def playerChoice():
  '''
  No input parameters needed.
  Function should ask the players to make their choice.  How you ask is unimportant, but the
  output must be consistent:
  0: rock
  1: paper
  2: scissors
  '''
  value = input("Enter your choice: \n")
  if value == "rock" or value == "Rock":
    value = 0
  if value == "papper" or value == "paper" or value == "Papper" or value == "Paper":
    value = 1
  if value == "scissors" or value == "Scissors":
    value = 2
  
  return value


if __name__ == "__main__":
  player = playerChoice()
  print(player)
