print("Welcome to the Odd or Even number checker! \n")

# get the number from user
get_number = int(input("Enter a number: "))

msg = ""

if get_number % 2 == 0:
    msg = "Even"
    if get_number == 0:
        msg = "Neither even nor an odd"
else:
    msg = "Odd"

# announce the result
print(f"{get_number} is an {msg} number. \n")