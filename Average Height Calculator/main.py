print("Welcome to the Average Height Calculator app! \n")

# Take input as a string first
input_heights = input("Enter the heights and separate them with a comma and a space: ")

# Convert the input string to a list of floats
heights = [float(height) for height in input_heights.split(", ")]

# Initialize variables to calculate the average
total_heights = 0
counter = 0

# Iterate over the list of heights
for height in heights:
    total_heights += height  # Add each height to the total
    counter += 1  # Increment the counter for each height

# Calculate the average height
average_height = total_heights / counter if counter != 0 else 0  # Prevent division by zero

# Output the average height
print(f"The average height is: {average_height}")
