# from replit import clear

#HINT: You can call clear() to clear the output in the console.

from art import logo
print(logo)

bids = {}
bidding_finished = False

def find_highedt_bidder(bidding_record):
    highedt_bid = 0
    winner = ""
    # bidding_record = {"Angela": 123, "James":321}
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highedt_bid: 
            highedt_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highedt_bid}")

while not bidding_finished:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    bids[name] = price

    should_continue = input("Are there any other bidders? Type 'yes' or 'no.\n")

    if should_continue == "no":
        bidding_finished = True
        find_highedt_bidder(bids)

    # elif should_continue == "yes":
    #     clear()