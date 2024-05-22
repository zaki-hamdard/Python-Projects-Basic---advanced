# Leap Year Checker

Welcome to the Leap Year Checker! This simple Python script allows you to check whether a given year is a leap year or not.

## How It Works

1. The script greets the user with a welcome message.
2. It prompts the user to input a year.
3. It checks if the entered year is a leap year:
    - A year is a leap year if it is divisible by 4.
    - However, if the year is also divisible by 100, it is not a leap year unless it is also divisible by 400.
4. It announces the result to the user.

## Code Explanation

```python
print("Welcome to the LEAP YEAR checker! \n")

# Get the year from the user
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

print(f"{get_year} is {msg} year \n")
