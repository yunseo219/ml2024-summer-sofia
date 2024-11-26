'''
The program asks the user for input N (positive integer) and reads it.
Then the program asks the user to provide N (x, y) pairs (one by one) and reads all of them: first: x value, then: y value for every pair one by one. 
X is treated as the input feature and Y is treated as the class label. X is a real number, Y is a non-negative integer.
This set of pairs constitutes the training set TrainS = {(x, y)_i}, i = 1..N.
Then the program asks the user for input M (positive integer) and reads it.
Then the program asks the user to provide M (x, y) pairs (one by one) and reads all of them: first: x value, then: y value for every pair one by one. 
X is treated as the input feature and Y is treated as the class label. X is a real number, Y is a non-negative integer.
This set of pairs constitutes the test set TestS = {(x, y)_i}, i = 1..M.
In the end, the program outputs: the best k for the kNN Classification method and the corresponding test accuracy. 
kNN Classifier should be trained on pairs from TrainS, tested on x values from TestS and compared with y values from TestS.
The basic functionality of data processing (data initialization, data insertion), should be done using Numpy library 
while the computation (ML) part should be done using Scikit-learn library as much as possible (note: you can combine with what you've done from the previous tasks). 
Note: you can try the following range of k: 1 <= k <= 10.
'''

import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import os

os.environ["LOKY_MAX_CPU_COUNT"] = "4" #To get rid of my errors

def main():
    N = int(input("Enter the input N (positive integer): "))
    if N <= 0:
        print("Error: N must be a positive integer.")
        return

    TrainS = np.zeros((N, 2))
    print("Enter the N (x, y) pairs (one by one):")
    for i in range(N):
        while True:
            x = float(input(f"Enter the real number x value: "))
            y = int(input(f"Enter the non-negative integer y value: "))
            if y >= 0:
                TrainS[i] = [x, y]
                break
            print("Error: y must be a non-negative integer.")

    X_train = TrainS[:, 0].reshape(-1, 1)  
    y_train = TrainS[:, 1]                

    while True:
        M = int(input("Enter the input M (positive integer): "))
        if M > 0:
            break
        print("Error: M must be a positive integer.")

    TestS = np.zeros((M, 2))
    print("Enter the M (x, y) test pairs:")
    for i in range(M):
        x = float(input(f"Enter the real number x value: "))
        y = int(input(f"Enter the non-negative integer y value: "))
        if y >= 0:
            TestS[i] = [x, y]

    X_test = TestS[:, 0].reshape(-1, 1) 
    y_test = TestS[:, 1]             

    #k: 1 <= k <= 10
    best_k = 1
    best_accuracy = 0
    max_k = min(10, N)  

    for k in range(1, max_k + 1):  
        knn = KNeighborsClassifier(n_neighbors=k)
        knn.fit(X_train, y_train)
        y_pred = knn.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        print(f"k = {k}, Test Accuracy = {accuracy:.2f}")
        if accuracy > best_accuracy:
            best_k = k
            best_accuracy = accuracy

    print(f"The best k is {best_k} with the best accuracy of {best_accuracy:.2f}")

if __name__ == "__main__":
    main()