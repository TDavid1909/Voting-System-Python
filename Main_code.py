#this is could be the main terminal but guys feel free if you want to create more
voting_list = True
already_voted = []
while voting_list:
    print("Enter your name")
    next_name = input()
    if next_name in already_voted:
        print("You cannot vote again")
    else:
        already_voted.append(next_name)
