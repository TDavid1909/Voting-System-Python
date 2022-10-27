#this is could be the main terminal but guys feel free if you want to create more
voter_id = [1,2,3,4,5,6,7,8]
name = str()
number_of_voter = len(voter_id) #this give the lengt of the list to know how many persons will vote
age = int()
democrats_votes = 0
republicans_votes = 0 
others = 0

def choose():
   print("You want to vote for the Governorship press P")
   print("You want to vote for the Senate press S")
   print("You want to vote for the House press H")
   print("You want to vote for the Governorship press G")
   house = input("Your option: ")
   house = house.upper()
   if house == "S":
      print("Thank you for your vote ", name)   #This is the function that run the nice part of the elections
   elif house == "P":
      print("Thank you for your vote ", name)
   elif house == "H":
      print("Thank you for your vote ", name)
   elif house == "G":
      print("Thank you for your vote ", name)
   
while True:
   condition = print(input("Would you like to vote? (Yes or NO)"))
   condition = condition.upper()
   if condition == "YES":
      str(input("What's your name?"))
      int(input("How old are you ?"))
      if age >= 18:
         voter = int(input("Enter your voter id: "))
         if voter in voter_id:
            print("You are a voter")
            voter_id.remove(voter)
            print("-------------------")
            print("To vote for repulicans press R")
            print("-------------------")
            print("To vote for Democrats press D")
            print("-------------------")
            print("To vote for other party press O")
            choise = input("Your choise: ")
            choise = choise.upper()
            if choise == "R":
               choose()
               republicans_votes = +1
            elif choise == "D":
               choose()
               democrats_votes = +1
            elif choise == "O":
               choose()
               others = +1                        
         else:
            print("You have already vote!")
      else:
         print("You need to be more 18 years old to vote!")
   else:
      break
   