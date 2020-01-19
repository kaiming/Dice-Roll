from random import randint

print("Welcome to Dice Sim")
print("How many sides would you like your first dice to have?")
dice1 = int(input())
print("How many sides would you like your second dice to have?")
dice2 = int(input())

min1 = 1
max1 = dice1

min2 = 1
max2 = dice2

repeat = True

while repeat:
  print("You rolled", randint(min1,max1), "for dice 1")
  print("You rolled", randint(min2,max2), "for dice 2")
  print("Do you want to roll again?")
  repeat = ("y" or "yes") in input().lower()
