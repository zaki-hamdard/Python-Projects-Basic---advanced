print("Welcome to the Roller Coaster Ticket calculator! \n")

get_name = input("Enter your name: ").title()
get_height = int(input("Please enter your height in cm. "))

can_ride = ""
bill = 0
photo_bill = 0

if get_height > 120:
    can_ride = "can ride"
    get_age = int(input("Please enter your age: "))

    if get_age > 18:
        bill = 12

    elif get_age in range (12, 18):
        bill = 7

    else:
        bill = 5

    want_photo = input("Do you want to take photos? ").lower()
    
    if want_photo == "yes":
        bill += 3
    
    print(f"Dear {get_name}! you {can_ride}, and your total bill is ${bill} \n")
    
else:
    can_ride = "connot ride"
    print(f"Sorry dear {get_name}. You {can_ride}")