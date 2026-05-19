# Create an error handling function
# Author: Loretta
# Date: 13 May 2026
# Version 3

'''# Code that tests that a valid number is entered (V1)
done = False # Boolean variable set to False
# While loop that runs until a valid number is entered
while not done:
    num = int(input("Please enter your number ( •̀ .̫ •́ )✧: "))
    done = True

print(f"The number you entered is {num} (´▽`ʃ♡ƪ).")'''

# Code that tests that a valid number is entered (V2)
# Create a function to call every time I ask the use for a number
# A function is a chuk of code that does something
# I can use a function over and over
# To use a function I 'call' it by writing out its name
'''def test_int_num():# test_int_num() is the name of the function
    done = False 
    while not done: 
        try: #This tries for a valid input
            num = int(input("Please enter your number( •̀ .̫ •́ )✧: "))
            done = True

        except ValueError:
            print("That is not a valid interger（；´д｀）ゞ.")

    return(num)

# Main routine
num_1 = test_int_num()
print(f"You entered {num_1} as your first number(❁´◡`❁).")

num_2 = test_int_num()
print(f"You entered {num_2} as your second number♪(´▽｀).")

print() # One way of creating a line break. \n also creates a line break.

sum = num_1 + num_2
print(f"\nYour two numbers added together are {sum} (´▽`ʃ♡ƪ)")

multiply = num_1 * num_2
print(f"Your two numbers multiplied with each other results in {multiply} (´▽`ʃ♡ƪ)")

#division
divide = num_1 / num_2
print(f"{num_1} divided by {num_2} is equal to {divide}")'''

# Version 3 Refining my code. maing it more pythonic
#This will result in being able to change the question in the function
def test_int_num(question, low, high): # 'question' is a placeholder
    done = False
    error = f"That is not an interger betweem {low} and {high}."
    while not done:
        # print(question)
        try: # tries valid input
            num = int(input(question))
            if num >= low and num <= high:
                done = True

            else:
                print(error)
                print()

        except ValueError:
            print(error)
    return(num)

# Main route
num_1 = test_int_num("Please enter your first number between 1 and 1000000: ", 1, 1000000 )
print(f"You entered {num_1} as your first number.\n")

num_2 = test_int_num("Please enter your second number between 1 and 1000000: ", 1, 1000000 )
print(f"You entered {num_2} as your second number.\n")

num_3 = test_int_num("Please enter your third number between 1 and 1000000: ", 1, 1000000 )
print(f"You entered {num_3} as your third number.\n")

sum = num_1 + num_2 + num_3
print(f"\nYour three numbers added together are {sum} (´▽`ʃ♡ƪ)\n")

multiply = num_1 * num_2 * num_3
print(f"Your three numbers multiplied with each other results in {multiply} (´▽`ʃ♡ƪ)\n")

#division
divide = num_1 / num_2 / num_3
print(f"{num_1} divided by {num_2} and {num_3} is equal to {divide}\n")