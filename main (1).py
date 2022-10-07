# Codebreaker game
# Jackson Blackman
# 2022-10-6

# imports
import random
from time import sleep

# lists
codelist = []
guesslist = []
correctguess = []

# Functions
def getcodelength():
  global codelength
  code = random.randint(100, 999999)
  codelength = str(code)
  for c in codelength:
    codelist.append(c)

def guessing():
    for c in codelength:
      guess = str(input('What is your guess \n:'))
      guesslist.append(guess)
      if guess == c:
        correctguess.append(c)
        print(str(c), 'is correct')
        guesschecker()
      elif guess:
        correctguess.append('X')

def guesschecker():
  if correctguess == codelist:
    print('you win')
    sleep(10)
    exit()

def guessclear():
  correctguess.clear()
  guesslist.clear()

# code
getcodelength()
while True:
  guessing()
  print(guesslist)
  print(correctguess)
  guessclear()