# print a welcome message
print("Welcome to the Tip Calculator App! \n")

# get the total bill
total_bill = float(input("What is the total bill? $"))

# how much tip to pay
tip = int(input("How much do you want to tip? 10, 12, or 15? "))

# how many people to split the bill between
split_between = int(input("How many people to split? "))

def tip_calculator():
    # add tip to the total bill
    bill_with_tip = total_bill * (tip/ 100) + total_bill

    # final bill to be paid by all the members with 2 decimal places
    final_bill = "{:.2f}".format((bill_with_tip / split_between))

    #output the result
    print(f"Each Person should pay: ${final_bill}")

tip_calculator()