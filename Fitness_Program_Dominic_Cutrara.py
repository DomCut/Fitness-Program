# Dominic Cutrara Homework 1, 2/14/24
# This program manages a weekly fitness schedule. It displays the current schedule,
# allows users to update activities, add new days, or exit the program.
# The schedule is stored in a dictionary.

# Dictionary to store the ten day fitness schedule starting Monday 
fitness_schedule = {
    "Monday": "Chest, compound lift",
    "Tuesday": "Back, compound lift",
    "Wednesday": "Cardio, running",
    "Thursday": "Legs, compound lift",
    "Friday": "Rest, cheat day",
    "Saturday": "Shoulders, hypertrophy",
    "Sunday": "Biceps, hypertrophy",
    "Next Monday": "Cardio, swimming",
    "Next Tuesday": "Back, hypertrophy",
    "Next Wednesday": "Legs, hypertrophy"
}

# Function to display the fitness schedule
def display_schedule():
    print("Current Fitness Schedule:")
    for day, activity in fitness_schedule.items():
        print(day + ": " + activity)

# Function to run the fitness program
def run_fitness_program():
    fitness_user_input = input("Do you want to 'update' the schedule, 'add' a new day, or 'exit'? ").lower()

    # Updating the fitness schedule
    if fitness_user_input == 'update':
        day_to_update = input("Enter the day you want to update: ").capitalize()
        if day_to_update in fitness_schedule:
            new_activity = input("Enter the new activity for " + day_to_update + ": ")
            fitness_schedule[day_to_update] = new_activity
            print(day_to_update + " activity updated to " + new_activity)
        else:
            print("Invalid day. Please enter a valid day of the week.")

    # Adding a new day to the fitness schedule
    elif fitness_user_input == 'add':
        new_day = input("Enter the new day to add: ").title()
        new_activity = input("Enter the activity for " + new_day + ": ")
        fitness_schedule.update({new_day: new_activity})
        print(new_day + " added with activity " + new_activity)

    # Exiting the program
    elif fitness_user_input == 'exit':
        print("Exiting the fitness schedule program.")
        return

    # Invalid input
    else:
        print("Invalid input. Please enter 'update', 'add', or 'exit'.")

    # So the program runs continuously 
    run_fitness_program()

# Display the fitness schedule immediately for reference
display_schedule()

# Start the fitness program
run_fitness_program()

# Display the final fitness schedule
print("\nFinal Fitness Schedule:")
display_schedule()
print("Enjoy your workout!")
