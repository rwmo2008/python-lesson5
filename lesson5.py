#def <function name> (<params>):
#    <Doc string>
#   <function code>

def print_welcome():
    """This function prints 2 lines of text"""
    print ("Welcome to my program")
    print ("I hope you like it")

print_welcome()
print()
print("To say it again")
print()
print_welcome()

print()
#passing values

def print_value(value):
    """This function prints a value"""
    print(value)

print_value(5)
print_value("number")

name = "Robert"
print_value(name)

print()

def change_value(value):
    """This function changes the value passed in to 1"""
    print ("Inside, value:", value)
    value = 1
    print ("Inside, value is changed to:", value)

number = 5
print("Outside, number is:", number)
change_value(number)
"""Value doesn't change"""
print("Outside, number is now:", number)

print()


#global variables
def change_number():
    """This function changes the value passed in to 1 (global)"""
    global number
    number = 1

number = 4
print ("Outside, number is:", number)
change_number()
print ("Outside, number is now:", number)
print()

#returning values from functions
#def square(num):
#default arguments
def square(num = 1):
    """This function calculates the square of a number"""
    result =num * num
    return result

print(square())
for i in range(1,11):
    print(square(i))

print()

#all Python functions return a value
#can return "None" if function is called and has no return statement
def print_welcome():
    """This function prints 2 lines of text"""
    print("Welcome to my program")
    print("I hope you like it")

print(print_welcome())
print()

#default arguments
def prompt_user(prompt, num_tries = 2):
    """This function prompts the user a certain number of times"""
    answer = input(prompt)

    while (answer != "yes" and answer != "no" and num_tries > 1):
       num_tries = num_tries - 1
       print ("Try again")
       answer = input(prompt)
       
prompt_user("Enter yes or no: ")
prompt_user("enter yes or no: ", 3)

prompt_user(prompt="Hello")
prompt_user(num_tries=3, prompt="Hi. Go again? ")
