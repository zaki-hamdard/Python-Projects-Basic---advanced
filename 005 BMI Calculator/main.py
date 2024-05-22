print("Welcome to the BMI Calculator! Check your Body Mass Index right now.")
print()

# 1st, get the height in meter; e.g: 1.72
get_height = float(input("What is your height in meter? \n"))

# 2nd, get the weight in KG; e.g: 70kg
get_weight = int(input("What is your weight in KG? \n"))

bmi = 0
msg = ""

#Check if the user is underweight, overweight or normal
def calc_bmi():
    # Calculate the BMI
    bmi = get_weight / (get_height * get_height)
    if bmi < 18:
        msg = "Underweight. Need to gain some weight."
    elif bmi >= 18 and bmi <= 25:
        msg = "Athelete! Your body mass index is perfect."
    else:
        msg = "Too Overweight. Please try to excercise more and eat less. "
# print the output
    print(f"Your BMI is {bmi}, {msg}")

# call the function for to calculate the BMI
calc_bmi()