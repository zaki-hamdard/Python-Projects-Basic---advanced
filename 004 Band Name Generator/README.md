# Band Name Generator App

Welcome to the Band Name Generator App! This simple Python program helps you create a unique band name by combining the name of the city you grew up in with the name of your pet.

## How It Works

1. **Input**: The program prompts you to enter the name of the city you grew up in and the name of your pet.
2. **Output**: It then generates a band name by combining these two inputs.

## Usage

1. Run the program.
2. When prompted, enter the name of the city you grew up in.
3. Enter the name of your pet when prompted.
4. The program will display your potential band name.

## Example

```python
print("Welcome to the Band Name Generator App!")

# Get the name of the city and pet from user
city_name = input("What is the name of the city you grew up in? \n")
pet_name = input("What is the name of your pet? \n")

print(f"Your band name could be {city_name} {pet_name}")

Welcome to the Band Name Generator App!

What is the name of the city you grew up in? 
New York
What is the name of your pet? 
Buddy

Your band name could be New York Buddy