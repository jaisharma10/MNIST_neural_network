import numpy as np

class LinearRegression:
    def __init__(self):
        pass

    def fit(self, X,y):
        samples, _ = X.shape
        A_mat = np.ones((samples,1))
        A_mat = np.hstack((A_mat, X))

        thet_predict = np.linalg.pinv(np.dot(A_mat.T, A_mat)).dot(A_mat.T).dot(y)
        return np.array(thet_predict)

    def predict(self, X, W):
        samples, _ = X.shape
        A_mat = np.ones((samples,1))
        print(A_mat.shape, X.shape)
        A_mat = np.hstack((A_mat, W))
        return X.dot(W)     


