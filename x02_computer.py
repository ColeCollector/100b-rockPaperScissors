#!python3
"""
Create a function that creates a random choice for the computer player:
input parameters: none required
output:

0 : rock
1 : paper
2 : scissors
"""
import random

def computerChoice():
  value = random.randint(0,2)
  return value

if __name__ == "__main__":
  computer = computerChoice()
  print(computer)
