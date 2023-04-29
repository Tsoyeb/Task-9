# This code will allow the user to either do a new calculation or print the results from a existing file. 

# Variable name of file saved outside of the loop as none to enable user to insert a name to this variable. 
file_name=None

# Asks user if they want to do a calculation or open a file. 
main_choice = input('Would you like to do a calculation?\nIf yes press Y key or any key to open a file:\n')
if main_choice.lower() != 'y':
    while True:
        try:
            file_name = input('Please enter the name of the file you wish to open:\n')
            with open(file_name, 'r') as f:
                print(f.read())
                break
        except FileNotFoundError:
            print(f'{file_name} does not exist, please re-enter the file name')
            continue

# Asks the user to enter numbers and operator. If input is not a integer the user will be told to start again.
else:
    while True:
        try:
            num_1 = int(input('Please enter first number:\n '))
            num_2 = int(input('Please enter your second number:\n '))
            operator = input('Please enter an operator e.g + - * /: \n ')
            
            if operator == '+':
                result = num_1 + num_2
            elif operator == '-':
                result = num_1 - num_2
            elif operator == '*':
                result = num_1 * num_2
            elif operator == '/':
# This block of code will handle the zero division error. 
# If the 1st number is divided by the 2nd number a error message will print and then the user will be promted to re-enter both numbers.
                condition = True
                while condition: 
                    try:
                        result = num_1 / num_2
                        condition = False
                    except ZeroDivisionError:
                        print('please try again without the Zero')
                        num_1 = int(input('Please enter first number:\n '))
                        num_2 = int(input('Please enter your second number:\n '))
                    
            else:
                print('Oops! Incorrect input, please start again')
                continue

        # Prints equation and answer    
            answer = (str(num_1) +' '+ str(operator) +' '+ str(num_2) + ' = ' + str(result))
            print(answer)
        
        except ValueError:
            print('Oops! Incorrect input, please start again')
            continue

# Asks the user to name the file and then saves file in documents. If file already exists the file will be appended.      
        if not file_name:
            file_name = input('Please enter a file name: ')

        with open(file_name, 'a') as f:
            f.write(answer + '\n')


# Asks the user if they want to add more equations:
            choice = input('Do you want to add another equation, Please enter Y/N:')
            if choice.lower() == 'y':
                continue
            else:
                break
