# print a welcoming message
print("Welcome to the Life in Week app! \n")

# get the user's name and age
get_name = input("What is your name? \n")
get_age = int(input("How old are you?. \n"))

# total number of weeks a person can live in 70 years
total_weeks_in_70_years = 52 * 70

# total number of weeks a person lived since the birthdate
weeks_lived = get_age * 52

# how many more weeks to live
weeks_remaining = total_weeks_in_70_years - weeks_lived

# print the output
print(f"Dear {get_name}! You lived {weeks_lived} weeks, and you will live only for {weeks_remaining} more weeks.")



      