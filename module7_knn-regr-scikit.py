'''
The program asks the user for input N (positive integer) and reads it.
Then the program asks the user for input k (positive integer) and reads it.
Then the program asks the user to provide N (x, y) points (one by one) and reads all of them: first: x value, then: y value for every point one by one. X and Y are the real numbers.
In the end, the program asks the user for input X and outputs: the result (Y) of k-NN Regression if k <= N, or any error message otherwise.
Additionally, provide the variance of labels in the training dataset.
The basic functionality of data processing (data initialization, data insertion), should be done using Numpy library 
while the computation (ML) part should be done using Scikit-learn library as much as possible (note: you can combine with what you've done from the previous task).

Additional reference: https://www.geeksforgeeks.org/k-nearest-neighbors-knn-regression-with-scikit-learn/
'''

import numpy as np
from sklearn.neighbors import KNeighborsRegressor
import os
os.environ["LOKY_MAX_CPU_COUNT"] = "4"  #To get rid of my errors


def main():
    N = int(input("Enter the input N (positive integer): "))
    k = int(input("Enter the input k (positive integer): "))
    if k > N:
        print("Error: k cannot be greater than N.")
        return
    
    points = np.zeros((N, 2))
    print("Enter the N (x, y) points:")

    for i in range(N):
        x = float(input(f"Enter the Real Number x for point {i+1}: "))
        y = float(input(f"Enter the Real Number y for point {i+1}: "))
        points[i] = [x, y]

    variance = np.var(points[:, 1])
    print(f"The variance is: {variance}")

    X = float(input("Enter the input X for result (Y) of k-NN Regression: "))

    result = knn_regression(points, k, X)
    print(f"The predicted Y value for X={X} is: {result}")

def knn_regression(points, k, X):
    X_train = points[:, 0].reshape(-1, 1) 
    y_train = points[:, 1]
    knn = KNeighborsRegressor(n_neighbors=k)
    knn.fit(X_train, y_train)
    y_predict = knn.predict(np.array([[X]]))
    return y_predict[0]

if __name__ == "__main__":
    main()
