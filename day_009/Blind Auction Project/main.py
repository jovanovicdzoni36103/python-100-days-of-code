# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added

bids = {}
continue_bidding = True

while continue_bidding:
    name = input("Enter your name: ")
    price = float(input("Enter your price: $"))
    bids[name] = price

    should_continue = input("Would you like to continue? (y/n): ").lower()
    if should_continue == "y":
        print("\n" * 20)  # Clears the screen for the next bidder
    elif should_continue == "n":
        continue_bidding = False


# TODO-4: Compare bids in dictionary
def find_highest_bidder(bidding_dictionary):
    highest_bid = 0
    winner = ""

    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print(f"The winner is {winner} with a bid of ${highest_bid}")


# znaci prodje sve i onda poziv funckije
find_highest_bidder(bids)