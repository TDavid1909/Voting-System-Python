#this is could be the main terminal but guys feel free if you want to create more


voter_id = [1,2,3,4,5,6,7,8]

number_of_voter = len(voter_id) #this give the lengt of the list to know how many persons will vote



while True:
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
            print("You want to vote for the Governorship press P")
            print("You want to vote for the Senate press S")
            print("You want to vote for the House press H")
            print("You want to vote for the Governorship press G")
            house = input("Your option: ")
            house = house.upper()
            if house == "S":
                print("Thank you for your vote")
            elif house == "P":
                print("Thank you for your vote")
            elif house == "H":
                print("Thank you for your vote")
            elif house == "G":
                print("Thank you for your vote")
        elif choise == "D":
             print("You want to vote for the Governorship press P")
             print("You want to vote for the Senate press S")
             print("You want to vote for the House press H")        #For all this block we could create some functions to make it less complicated
             print("You want to vote for the Governorship press G")
             house = input("Your option: ")
             house = house.upper()
             if house == "S":
                print("Thank you for your vote")
             elif house == "P":
                print("Thank you for your vote")
             elif house == "H":
                print("Thank you for your vote")
             elif house == "G":
                print("Thank you for your vote")
        elif choise == "O":
             print("You want to vote for the Governorship press P")
             print("You want to vote for the Senate press S")
             print("You want to vote for the House press H")
             print("You want to vote for the Governorship press G")
             house = input("Your option: ")
             house = house.upper()
             if house == "S":
                print("Thank you for your vote")
             elif house == "P":
                print("Thank you for your vote")
             elif house == "H":
                print("Thank you for your vote")
             elif house == "G":
                print("Thank you for your vote")
            
            
    else:
        print("You've already voted")
