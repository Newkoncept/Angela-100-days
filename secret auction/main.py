import art

print("Welcome to Py Secret Auction")
print(art.logo)
bidder_details = {}

while True:
    user_name = input("What is your name?: ")
    user_bid = int(input("What's your bid: $"))
    program_continue = input("Are there any other bidders? Type 'yes' or 'no'\n").lower()

    bidder_details[user_name] = user_bid

    if program_continue == "no":
        print("\n"*100)

        winner_name = ""
        winning_bid = 0
        for i in bidder_details:
            if bidder_details[i] > winning_bid:
                winner_name = i
                winning_bid = bidder_details[i]
        print(f"The winner of the bid is {winner_name} with ${winning_bid}")
        break
    elif program_continue == "yes":
        print("\n"*100)



