# Task 1: 
# Your Mood Tracker 
# Simulate a mood tracker that records your mood at three 
# different times of the day (morning, afternoon, evening) 
# for each day of the week. Use nested loops to implement this: 
# the outer loop should iterate over the days, and the inner 
# loop should iterate over the times of the day. 
# For each time, randomly select a mood from a predefined list 
# and print it. Use the random module again to randomly select 
# the mood.

# Example Outcome: An example would be "On Tuesday afternoon 
# you were sad" "On Tuesday night you were happy" 
# "On Wednesday morning you were tired"

# Answer:
import random

# Predefined list of moods
moods = ["happy", "sad", "tired", "excited", "angry", "relaxed"]

# Days of the week
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# Times of the day
times = ["morning", "afternoon", "evening"]

# Nested loops to iterate over days and times
for day in days:
    for time in times:
        mood = random.choice(moods)
        print(f"On {day} {time} you were {mood}")
