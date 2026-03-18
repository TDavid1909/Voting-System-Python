voter_ids = {1,2,3,4,5,6,7,8}

dem_votes = 0
rep_votes = 0
other_votes = 0

senate_votes = 0
house_votes = 0
governor_votes = 0


def choose_house(name):
    global senate_votes, house_votes, governor_votes

    print("-----------------------------------")
    print("Vote for Senate: S")
    print("Vote for House: H")
    print("Vote for Governorship: G")
    print("-----------------------------------")

    option = input("Your option: ").upper()

    if option == "S":
        senate_votes += 1
    elif option == "H":
        house_votes += 1
    elif option == "G":
        governor_votes += 1
    else:
        print("Invalid option.")
        return choose_house(name)

    print(f"Thank you for your vote, {name}!")


while True:
    condition = input("Would you like to vote? (Yes or No): ").upper()

    if condition != "YES":
        break

    name = input("What's your name? ")
    age = int(input("How old are you? "))

    if age < 18:
        print("You must be at least 18 years old to vote.")
        continue

    voter = int(input("Enter your voter ID: "))

    if voter not in voter_ids:
        print("You have already voted or ID is invalid.")
        continue

    voter_ids.remove(voter)

    print("-------------------")
    print("Vote Republican: R")
    print("Vote Democrat: D")
    print("Vote Other: O")
    print("-------------------")

    choice = input("Your choice: ").upper()

    if choice == "R":
        rep_votes += 1
        print("Republican vote recorded.")
    elif choice == "D":
        dem_votes += 1
        print("Democrat vote recorded.")
    elif choice == "O":
        other_votes += 1
        print("Other vote recorded.")
    else:
        print("Invalid choice.")
        continue

    choose_house(name)


# Final Results
print("-----------------------------------")
print("Total Remaining Voters:", len(voter_ids))
print("-----------------------------------")
print("Democrat Votes:", dem_votes)
print("Republican Votes:", rep_votes)
print("Other Votes:", other_votes)
print("-----------------------------------")

# Winner (classroom simulation only)
if dem_votes > rep_votes and dem_votes > other_votes:
    print("Democrats received the most votes.")
elif rep_votes > dem_votes and rep_votes > other_votes:
    print("Republicans received the most votes.")
elif other_votes > dem_votes and other_votes > rep_votes:
    print("Other party received the most votes.")
else:
    print("No clear winner.")

print("-----------------------------------")
print("Senate Votes:", senate_votes)
print("House Votes:", house_votes)
print("Governorship Votes:", governor_votes)
print("-----------------------------------")
