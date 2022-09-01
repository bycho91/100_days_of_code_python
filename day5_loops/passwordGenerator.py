#Password Generator Project
from os import lstat
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def generateRandomString(num, arr):
   str = ""
   for i in range(0, num):
      str += arr[random.randrange(0, len(arr))]
   
   return str

def shuffleString(str):
   return random.shuffle([c for c in str]).join()

def generatePassword():
   print('Welcome to the random password generator!')
   
   
   # GET USER INPUT
   numLetters = int(input('How many letters would you like in your password?\n'))
   numNumbers = int(input('How many numbers would you like in your password?\n'))
   numSymbols = int(input('How many symbols would you like in your password?\n'))
   
   # GENERATE AND ASSIGN RANDOM STRINGS BASED ON USER INPUT
   lettersStr = generateRandomString(numLetters, letters)
   numbersStr = generateRandomString(numNumbers, numbers)
   symbolsStr = generateRandomString(numSymbols, symbols)
   
   randomPasswordStr = f'{lettersStr}{numbersStr}{symbolsStr}'
   
   pArr = [c for c in randomPasswordStr]
   
   random.shuffle(pArr)
   
   shuffledPassword = ""
   for c in pArr:
      shuffledPassword += c
   
   return shuffledPassword
   
   
   
   
   
generatePassword()