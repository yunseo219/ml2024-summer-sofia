'''
The program asks the user for input N (positive integer) and reads it
Then the program asks the user to provide N numbers (one by one) and reads all of them (again, one by one)
In the end, the program asks the user for input X (integer) and outputs: "-1" if there were no such X among N read numbers, 
or the index (from 1 to N) of this X if the user inputed it before.
'''

# Asking the user for the integer N
N = int(input("Enter the input N (positive integer): "))

# Creating empty list to track
user_input = []

# Asking the user to provide N
for i in range(N):
    number = int(input(f"Enter {N} numbers - #{i+1}: "))
    user_input.append(number)

# Asking the user for the integer X
X = int(input("Enter the input X (integer): "))

# Checking if X is in the user inputs
if X in user_input:
    print(f"Index of {X} is found at the position: #{user_input.index(X) + 1}")
else:
    print("-1")
