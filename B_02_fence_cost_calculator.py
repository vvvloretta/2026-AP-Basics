# Create a fence cost calculator
# Author: Loretta Qi
# Date: 3 June 2026
# Version 1

def num_check(question):
    error = "Please enter a number that is more than zero\n"
    while True:

        try:
            # Ask the user for a number
            response = float(input(question))

            # Check that the number is more than zero
            if response > 0:
               return response
            else:
                print(error)

        except ValueError:
            print(error)


# Main Routine starts here...

keep_going = ""
while keep_going == "":
    # Get width and height
    width = num_check("Width: ")
    length = num_check("length: ")
    cost = width * length
    
    cost_per_metre = num_check("Cost per metre: ")

    # Calculate perimeter and price for the fence
    perimeter = (width + length) * 2
    price = perimeter * cost_per_metre

    # Display output
    print()
    print(f"Perimeter: {perimeter} metres")
    print(f"Price: ${price:.2f}")

     # Ask user if they want to keep going
    keep_going = input("Press enter to keep going or any key to quit. ")
    print()

print("Thank you for using fence cost calculator.")