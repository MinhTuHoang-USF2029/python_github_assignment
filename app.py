# Welcome Message
print("Welcome to my Python program!")

# Input studying hours today
hours = input("How many hours did you study today? ")

# Convert input into float and calculate the estimated studying hours this week
hours = float(hours)
weekly_hours = hours * 7

# Remind how many hours to study this week
print(f"You are on track to study {weekly_hours} hours this week")

# Handle incorrect user input's type error
try:
    hours = float(hours)
except ValueError:
    print("Please enter a valid number.")
    exit()





