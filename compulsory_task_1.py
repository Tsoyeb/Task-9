# A simple calculator program which will take two numbers and a operator from the user and return the answer.


# Variable name of file saved outside of the loop as none to enable user to insert a name to this variable. 
file_name=None


# Asks the user to enter numbers and operator. If input is not a integer the user will be told to start again.
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
        answer = (str(num_1) +' '+ str(operator)+' '+ str(num_2) + ' = ' + str(result))
        print(answer)
        
    except ValueError:
        print('Oops! Incorrect input, please start again')
        continue

# Asks the user to name the file and then saves file in documents. If file already exists the file will be appended.   
    open_mode = 'a'
    if not file_name:
        file_name = input('Please enter a file name:\n ' )
        open_mode = 'w'

    with open(file_name, open_mode) as f:
            f.write(answer + '\n')
            f.close

# Asks the user if they want to add more equations:
    choice = input('Do you want to add another equation, Please enter Y/N:')
    if choice.lower() == 'y':
        continue
    else:
        break
