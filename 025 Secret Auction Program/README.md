
# Secret Auction Program

Welcome to the Secret Auction Program! This simple Python script allows users to conduct a secret auction where multiple bidders can place their bids anonymously. The program will determine and announce the highest bidder once all bids are entered.

## How It Works

1. **Start the Program:** When the script is run, it welcomes the user to the Secret Auction Program.

2. **Enter Bidder Information:** The program will prompt the user to enter the name and bid amount for each bidder.

3. **Check for Additional Bidders:** After each bid, the program will ask if there are more bidders. If there are, the process repeats.

4. **Determine the Winner:** Once there are no more bidders, the program will determine and display the highest bid and the corresponding bidder's name.

## Usage

1. **Run the Script:** Execute the script in a Python environment.

```bash
python secret_auction.py
```

2. **Follow the Prompts:** Enter the bidder's name and bid amount when prompted. Indicate whether there are additional bidders when asked.

3. **View the Results:** Once all bids are entered, the program will display the highest bid and the bidder's name.

## Example

```
Welcome to the Secret Auction Program!

What is the bidder's name? Alice
How much do you want to bid? $150
Is there another bidder? Type 'yes' or 'no': yes

What is the bidder's name? Bob
How much do you want to bid? $200
Is there another bidder? Type 'yes' or 'no': no

Bob has the highest bid of $200
```

## Code

```python
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
```

## Requirements

- Python 3.x

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
