'''
The program asks the user for input N (positive integer) and reads it.
Then the program asks the user to provide N (x, y) points (one by one) and reads all of them: first: x value, then: y value for every point one by one. 
X is treated as the ground truth (correct) class label and Y is treated as the predicted class. Both X and Y are either 0 or 1.
In the end, the program outputs: the Precision and Recall based on the inputs.
The basic functionality of data processing (data initialization, data insertion), should be done using Numpy library 
while the computation (ML) part should be done using Scikit-learn library as much as possible (note: you can combine with what you've done from the previous tasks).

'''

import numpy as np
from sklearn.metrics import precision_score, recall_score

def main():
    N = int(input("Enter the input N (positive integer): "))
    if N <= 0:
        print("Error: N must be a positive integer.")
        return

    points = np.zeros((N, 2), dtype=int)
    print("Enter the N (x, y) points:")
    
    for i in range(N):
        x = int(input(f"Enter the {i+1} point Ground Truth x (0 or 1): "))
        y = int(input(f"Enter the {i+1} point Predicted y (0 or 1): "))
        
        if x not in (0, 1) or y not in (0, 1):
            print("Please enter either 0 or 1")
            return
        
        points[i] = [x, y]
    
    ground_truth = points[:, 0]
    predictions = points[:, 1]

    precision = precision_score(ground_truth, predictions)
    recall = recall_score(ground_truth, predictions)

    print(f"Precision: {int(precision)}")
    print(f"Recall: {int(recall)}")

if __name__ == "__main__":
    main()
