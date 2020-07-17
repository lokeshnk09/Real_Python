from random import randint


def rolling_dice():
  minimum = 1
  maximum = 6

  roll_dice = True
  while roll_dice:
    print("Rolling dice...")
    result = randint(minimum, maximum)
    roll_dice = False
    repeater = input("Do you want to roll again :(yes or no)?: ").lower()
    while repeater not in ["yes", "no"]:
      repeater = input("Invalid input. Please try again: ").lower()
      if repeater == 'yes':
        roll_dice = True
      elif repeater == "no":
        roll_dice = False
        print("Have a good day.")


c = rolling_dice()
