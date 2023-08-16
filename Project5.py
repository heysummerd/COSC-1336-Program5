#---------------------
# Summer Davis
# COSC 1336
# Project 5
#---------------------
# Objective: Program will calculate the total distance a vehicle
# has covered for each hour it has traveled.
#
# Program will:
# -ask user to enter the speed of a vehicle (in miles per hour).
# -ask user how many hours the vehicle has traveled.
# -validate that the inputs are positive.
# -calculate and display total distance the vehicle has traveled
#  for each hour of the period.
# 
#---------------------

# Display the start of the project
def header ():
    print('\n')
    print('Driver\'s Entry')
    print('-' * 80)

# Collect and organize all of the program tasks
def main():
    
    # Header of the project
    header()

    # Collect speed and hours traveled
    speed, hours = getVehicleData()

    # Display distance traveled summary
    generateTravelSummary(speed, hours)
    
    # End of project display
    footer()

# Generate a summary for each hour traveled
def generateTravelSummary(speed, hours):
    print('\n')
    print('-' * 80)
    print('Distance Traveled Summary')
    print('-' * 80)
    print(f'\nHour     Distance Traveled (miles)')
    print('-' * 40)

    for hour in range(1, hours + 1):
        miles = hour * speed
        print(f'{hour:<15} {miles:<20}')


# Collect and validate both the speed and hours traveled
def getVehicleData():
    speed = getIntegerEntry('What is the speed of the vehicle in mph: ')
    hours = getIntegerEntry('How many hours has it traveled? ')
    return speed, hours

# Get users entry of string data
def getStringEntry(prompt):
    while (True):
        value = input(prompt)
        return  value


# Get users entry of ONLY float data
def getFloatEntry(prompt):
    while (True):
        try:
            value = float(input(prompt))
            return value

        except ValueError: 
            print('\n\tError: Non Numbers entered.\n')

# Get users entry of ONLY integer data
def getIntegerEntry(prompt):
    while (True):
        try:
            value = int(input(prompt))
            if (value >= 0):
                return value
            else:
                print('\n\tError: Negative numbers entered. Please enter positive numbers.\n')

        except ValueError: 
            print('\n\tError: Non Integers entered. Please enter whole numbers.\n')
    
# Display the end of the project
def footer():
    print('\n')
    print('-' * 80)
    print('End of Project 5')

# Call the main function  
main()
