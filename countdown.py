# Countdown using a while loop

# Input: Get the starting number from the user
start_number = int(input("Enter a starting number for the countdown: "))

# Ensure the starting number is positive
if start_number <= 0:
    print("Please enter a positive starting number.")
else:
    # While loop for countdown
    while start_number > 0:
        print(start_number)
        start_number -= 1  # Decrement the number

    print("Blastoff!")
