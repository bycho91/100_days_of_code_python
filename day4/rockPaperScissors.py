import random

def determineWinner(human, computer):
   if(human.lower() == "rock"):
      if(computer == "rock"):
         return 'TIE'
      elif(computer == "paper"):
         return f"CPU wins with {computer}"
      else:
         return f"Human wins with {human}"
   elif(human.lower() == "paper"):
      if(computer == "paper"):
         return 'TIE'
      elif(computer == "rock"):
         return f"Human wins with {human}"
      else:
         return f"CPU wins with {computer}"
   else:
      if(computer == "scissors"):
         return 'TIE'
      elif(computer == "rock"):
         return f"CPU wins with {computer}"
      else:
         return f"Human wins with {human}"

def playGame():
   print("Let's play a game \n")
   
   userChoice = input('Rock paper or scissors? \n')
   computer = random.random() * 3
   computerChoice = ""
   if(computer < 1):
      computerChoice = "rock"
   elif(computer < 2):
      computerChoice = "paper"
   else:
      computerChoice = "scissors"
   
   return determineWinner(userChoice, computerChoice)
      
print(playGame())