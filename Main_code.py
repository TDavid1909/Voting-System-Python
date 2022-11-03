#this is could be the main terminal but guys feel free if you want to create more
voter_id = [1,2,3,4,5,6,7,8]
name = str()
number_of_voter = len(voter_id) #this give the lengt of the list to know how many persons will vote
age = int()
democrats_votes = 0
republicans_votes = 0 
others = 0
total = str(democrats_votes + republicans_votes + others) #added total
senators_vote = 0
governor_vote = 0 #variable used to define all the houeses
house_vote = 0

def choose():
   global senators_vote
   global governor_vote
   global house_vote
   print("You want to vote for the Senate press S")
   print("You want to vote for the House press H")
   print("You want to vote for the Governorship press G")
   house = input("Your option: ")
   house = house.upper()
   if house == "S":
      senators_vote = +1
      print("Thank you for your vote ", name)   #This is the function that run the nice part of the elections
   elif house == "H":
      house_vote = +1
      print("Thank you for your vote ", name)
   elif house == "G":
      governor_vote = +1
      print("Thank you for your vote ", name)
   
while True:
   condition = input("Would you like to vote? (Yes or NO)")
   condition = condition.upper() 
   if condition == "YES":
    name = str(input("What's your name?"))
    age = int(input("How old are you ?"))
    if age >= 18:
        voter = int(input("Enter your voter id: "))
        if voter in voter_id:
            print("You are a voter")
            voter_id.remove(voter)
            print("-------------------")
            print("To vote for Republicans press R")
            print("-------------------")
            print("To vote for Democrats press D")
            print("-------------------")
            print("To vote for other party press O")
            choise = input("Your choise: ")
            choise = choise.upper()
            if choise == "R":
               republicans_votes = republicans_votes+1 #added republicans to add one per input
               print("Republican Votes: " + str(republicans_votes))#added to show republican votes
               choose()
            elif choise == "D":
               democrats_votes = democrats_votes+1 #added democrats to add one per input
               print("Democrat Votes: " + str(democrats_votes))#added to show democrate votes
               choose()
            elif choise == "O":
               others = others+1 #added others to add one per input
               print("Other Votes: " + str(others)) #added to show other votes
               choose()
        else:
            print("You have already vote!")
    else:
         print("You need to be more 18 years old to vote!")
   else:
    break
   
print("-----------------------------------")
print("Total Voter: ", number_of_voter)
print("-----------------------------------")
print("Democrats votes: ", democrats_votes)
print("-----------------------------------")
print("Republicans votes: ", republicans_votes)
print("-----------------------------------")
print(others)
print("-----------------------------------")

if democrats_votes > republicans_votes and democrats_votes > others:
   print("The democrats had won the elections!!")
elif republicans_votes > democrats_votes and republicans_votes > others: #Main section of the elections of who wins
   print("The republicans had won the election!!")
elif others > democrats_votes and others > republicans_votes:
   print("Others had won the elections!!!")
else:
   print("There is not a clear winner!")

print("-----------------------------------")   
print("-----------------------------------")
print("Senate Votes: ", senators_vote)
print("-----------------------------------")
print("House Voters: ", house_vote)
print("-----------------------------------")
print("Governorship Votes: ", governor_vote)
print("-----------------------------------")
print("-----------------------------------")



   