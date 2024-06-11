print("Welcome to the Secret Auction Program!\n")

bidders = []  # List to store all bidders

should_continue = True
while should_continue:
    name = input("What is the bidder's name? ")
    bid_amount = int(input("How much do you want to bid? $"))

    # Store bidder information in a dictionary and add to the list
    bidder = {"name": name, "bid_amount": bid_amount}
    bidders.append(bidder)

    # Check if there is another bidder
    if input("Is there another bidder? Type 'yes' or 'no': ").lower() == "no":
        should_continue = False  # Exit the loop if no more bidders

# Find the highest bidder
greatest_bid = 0
greatest_bidder_name = ""
for bidder in bidders:
    if bidder["bid_amount"] > greatest_bid:
        greatest_bid = bidder["bid_amount"]
        greatest_bidder_name = bidder["name"]

print(f"{greatest_bidder_name} has the highest bid of ${greatest_bid}")
