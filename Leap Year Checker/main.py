print("Welcome to the LEAP YEAR checker! \n")

# get the year from user
get_year = int(input("Please enter a year: "))

if get_year % 4 == 0:
    if get_year % 100 == 0:
        if get_year % 400 == 0:
            msg = "leap"
        else:
            msg = "not leap"
    else:
        msg = "leap"

else: 
    msg = "not leap"

print(f"{get_year} is {msg} year \n ")