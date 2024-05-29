import math

h = int(input("What is the height of the wall? "))
w = int(input("What is the with of the wall? "))

coverage = 5

def paint_calc(height, width, coverage):

    can_nums = (height * width) / coverage

    print(f"You need {math.ceil(can_nums)}")


paint_calc(height = h, width = w, coverage = coverage)