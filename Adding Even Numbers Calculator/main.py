# Display a welcoming message
print("Welcome to the Adding Even Numbers Calculator! \n")

# get the target number from user
get_numbers = int(input("Enter a number between 0 and 500: "))

# Loop through the even numbers and add them to total
total = 0
for number in range(2, get_numbers + 1, 2):

    total += number

# Output the result
print(f"The total sum of the even numbers between 0 and {get_numbers} is {total}")
