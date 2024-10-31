'''
The program asks the user for input N (positive integer) and reads it
Then the program asks the user to provide N numbers (one by one) and reads all of them (again, one by one)
In the end, the program asks the user for input X (integer) and outputs: "-1" 
if there were no such X among N read numbers, or the index (from 1 to N) of this X if the user inputted it before.
The basic functionality of data processing (data initialization, data insertion, data search) should be done via Object-Oriented Programming Paradigm (i.e. using Classes)
'''

class NumberTracker:
    def __init__(self):
        self.numbers = []

    # Asking the user for the integer N
    def get_N(self):
        while True:
            n = int(input("Enter the input N (positive integer): "))
            if n > 0:
                return n
            else:
                print("Please enter a positive integer.")

    # Asking the user to provide N
    def get_numbers(self, n):
        for i in range(n):
            while True:
                try:
                    number = int(input(f"Enter {n} numbers - #{i + 1}: "))
                    self.numbers.append(number)
                    break
                except ValueError:
                    print("Invalid input. Please enter an integer.")

    # Checking if X is in the list
    def find_X(self, x):
        try:
            index = self.numbers.index(x)
            return index + 1
        except ValueError:
            return -1

    # Asking the user for the integer X
    def get_X(self):
        while True:
            try:
                return int(input("Enter the input X (integer): "))
            except ValueError:
                print("Invalid input. Please enter an integer.")