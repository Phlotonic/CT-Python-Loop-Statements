# Task 1: 
# Your Mood Today 
# Write a program that prints off different moods for each day 
# of the week. Create a list of moods such as "Happy", "Sad", 
# "Energetic", and "Calm". Using the range() function, loop 
# through every day of the week and for each day, randomly 
# select a mood from the list and print it. 
# Ensure that your program includes the use of the random 
# module to select the mood.

# Example Outcome: An example output could be 
# "On Wednesday, you were feeling happy." 
# "On Thursday you were feeling sad."

# Answer:

import random

# List of moods
moods = ["Happy", "Sad", "Energetic", "Calm"]

# List of days of the week
days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# Loop through each day of the week
for day in days_of_week:
    # Randomly select a mood from the list
    mood = random.choice(moods)
    # Print the mood for the day
    print(f"On {day}, you were feeling {mood}.")
