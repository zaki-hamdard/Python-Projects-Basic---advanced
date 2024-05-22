# Odd or Even Number Checker

Welcome to the Odd or Even Number Checker! This simple Python script allows you to check whether a given number is odd or even.

## How It Works

1. The script greets the user with a welcome message.
2. It prompts the user to input a number.
3. It checks if the entered number is odd or even:
    - If the number is divisible by 2, it's considered even.
    - If the number is not divisible by 2, it's considered odd.
    - Special case: If the number is 0, it is identified as "Neither even nor odd."
4. It announces the result to the user.

## Code Explanation

```python
print("Welcome to the Odd or Even number checker! \n")

# Get the number from the user
get_number = int(input("Enter a number: "))

msg = ""

if get_number % 2 == 0:
    msg = "Even"
    if get_number == 0:
        msg = "Neither even nor odd"
else:
    msg = "Odd"

# Announce the result
print(f"{get_number} is an {msg} number. \n")
