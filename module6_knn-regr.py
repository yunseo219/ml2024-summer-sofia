"""
The program asks the user for input N (positive integer) and reads it.
Then the program asks the user for input k (positive integer) and reads it.
Then the program asks the user to provide N (x, y) points (one by one) and reads all of them: 
first: x value, then: y value for every point one by one. X and Y are the real numbers.
In the end, the program asks the user for input X and outputs: the result (Y) of k-NN Regression if k <= N, or any error message otherwise.
The basic functionality of data processing (data initialization, data insertion, data calculation) should be done using Numpy library as much as possible.
"""

import numpy as np

def main():
    N = int(input("Enter the input N (positive integer): "))
    k = int(input("Enter the input k (positive integer): "))
    if k > N:
        print("Error: k cannot be greater than N.")
        return
    
    points = np.zeros((N, 2))
    
    print("Enter the N (x, y) points:")

    for i in range(N):
        x = int(input(f"Enter the Real Number x for point {i+1}: "))
        y = int(input(f"Enter the Real Number y for point {i+1}: "))
        points[i] = [x, y]

    X = int(input("Enter the input X for result (Y) of k-NN Regression: "))
    
    result = knn_regression(points, k, X)
    if result is not None:
        print(f"The predicted Y value for X={X} is: {result}")

def knn_regression(points, k, X):
    distances = np.abs(points[:, 0] - X)
    nearest_y = points[np.argsort(distances)[:k], 1]
    return np.mean(nearest_y)

if __name__ == "__main__":
    main()