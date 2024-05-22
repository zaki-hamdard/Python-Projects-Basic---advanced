# True Love Calculator App

Welcome to the True Love Calculator app! This fun and simple app calculates a "love score" based on the names of two individuals. The score is determined by counting the occurrences of specific letters in the combined names and applying a formula.

## How It Works

1. The user is prompted to enter their name and their lover's name.
2. The app combines both names and converts them to lowercase to ensure case insensitivity.
3. It counts the occurrences of the letters in the words "TRUE" and "LOVE" within the combined names.
4. The counts are used to form a two-digit score.
5. Based on the score, the app provides a message about the relationship.

## Calculation Details

- The letters `T`, `R`, `U`, and `E` are counted in the combined names.
- The sum of these counts forms the first digit of the score.
- The letters `L`, `O`, `V`, and `E` are counted in the combined names.
- The sum of these counts forms the second digit of the score.
- The final score is formed by concatenating the first and second digits.

## Score Interpretation

- **Score > 90 or < 10**: "Your score is {score}, you are dying for each other."
- **Score between 40 and 50 (inclusive)**: "Your score is {score}, you're alright together."
- **All other scores**: "Your score is {score}. I am sorry to have to tell you this, but you should give up on your lover."

## Getting Started

To run the True Love Calculator app, follow these steps:

1. Ensure you have Python installed on your system.
2. Copy the code below into a Python file (e.g., `true_love_calculator.py`).
