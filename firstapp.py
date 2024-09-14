# Height calculation using functions and user input, if input is not number/float, program will show error
# Use of try and except instead of if_else for validation and running

height_in_inch = 12             # Global variable

def height_in_unit(height_in_feet): # local variable inside the function, used only in function
    print(height_in_feet > 0)
    print(type(height_in_feet > 0))
    return f"{height_in_feet} feet = {height_in_feet * height_in_inch} inches"
    
def validate_and_run():

    try:
        
        user_input_number = float(user_input)
        if user_input_number > 0:
            calculate_value = height_in_unit(user_input_number)
            print(calculate_value)
        elif user_input_number == 0:
            print("You have entered 0, please input positive number")
        else:
            print("You have entered a -ve number, please input positive number")
    
    except ValueError:
        print("Your input is not number or float, please input valid positive number")

#while True:  # Application continue untill manually not stopped
user_input = ""
while user_input != "exit": # Application continue until user input is exit.
    user_input = input("Enter height in feet to convert in Inches and Centimeters :\n")     # Global variable
    validate_and_run()
