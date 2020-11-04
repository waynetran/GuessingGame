"""Number Guessing Game
To start the game call:
game.run()

You can optionally pass in the min, max and numAttempts args to configure different playing rules.

"""
import random

def promptForNumber():
  """Asks the user to guess a number

  Returns
  -------
  int
    The user input converted to an integer.

  """
  return int(input("\nPick a number between 1 and 1000: "))

def showWelcome():
  """Displays a welcome message on game start.
  """
  print("Welcome to the Guessing Game.")
  print("The object of the game is to guess a number between 1 and 1000 within 5 tries.")

def handleGuesses(answer, maxAttempts):
  """Handles logic for guessing a number within a number of attempts

  Parameters
  -------
  answer: int
    The correct answer to compare a guess with
  """

  print(f"You have {maxAttempts} guesses.")
  attempts = 0
  while attempts < maxAttempts:
    try:
      guess = promptForNumber()
      if guess > answer:
        print("smaller")
      elif guess < answer:
        print("bigger")
      else:
        print("correct!")
        return
    except ValueError:
      print(f"You didn't enter an integer. Please try again")
    except:
      print("I didnt' understand that. Please try again.")
    else:
      attempts+=1
  else:
    print(f"Sorry, you've run out of attempts. The answer is {answer}")

def promptKeepPlaying():
  """Asks the player (y/n) if they want to keep playing

  If the user enters "y", we return True, if "n", we return False

  Pseudocode:
  -----------
  loop while input is not correct
    answer = get user input "Play again? (y/n)"
    if answer is 'y'
      return True
    else if answer is 'n'
      return False

  Returns
  -------
  bool
    True if the player wants to play again, False otherwise.


  """

  correctInput = False
  while not correctInput:
    ans = input("Do you want to play again? (y/n)")
    if ans == 'y':
      return True
    elif ans == 'n':
      return False

def run(minNum=1, maxNum=1000, maxAttempts=5):
  keepPlaying = True
  while keepPlaying:
    #This is the number the user has to guess
    answer = random.randint(minNum,maxNum)
    showWelcome()
    handleGuesses(answer, maxAttempts)
    keepPlaying = promptKeepPlaying()