#this is could be the main terminal but guys feel free if you want to create more
voter_id = [1,2,3,4,5,6,7,8]

number_of_voter = len(voter_id)

while True:
    voter = int(input("Enter your voter id: "))
    if voter in voter_id:
        print("You are a voter")
        voter_id.remove(voter)
    
