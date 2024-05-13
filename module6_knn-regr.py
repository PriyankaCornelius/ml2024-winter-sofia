import numpy as np

def euclidean_distance(point1, point2):
    return np.sqrt(np.sum((point1 - point2) ** 2))

def knn_regression(X_train, y_train, X_test, k):
    distances = np.array([euclidean_distance(X_test, x_train) for x_train in X_train])
    nearest_indices = np.argsort(distances)[:k]
    nearest_y = y_train[nearest_indices]
    return np.mean(nearest_y)

def main():
    # Read input N (number of points)
    N = int(input("Enter the number of points (N): "))
    
    # Read input k (number of nearest neighbors)
    k = int(input("Enter the number of nearest neighbors (k): "))
    
    # Read N (x, y) points
    points = []
    for i in range(N):
        x = float(input(f"Enter x-coordinate of point {i+1}: "))
        y = float(input(f"Enter y-coordinate of point {i+1}: "))
        points.append([x, y])
    
    # Convert points to NumPy array
    points = np.array(points)
    
    # Separate X and y values
    X_train = points[:, 0]
    y_train = points[:, 1]
    
    # Read input X for prediction
    X_test = float(input("Enter the x-coordinate for prediction (X): "))
    
    # Perform k-NN regression
    if k <= N:
        y_pred = knn_regression(X_train, y_train, np.array([X_test]), k)
        print(f"Predicted y-coordinate (Y) for X = {X_test}: {y_pred}")
    else:
        print("Error: k should be less than or equal to N.")

if __name__ == "__main__":
    main()
