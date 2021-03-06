import numpy as np


def normal_eqn(X, y):
    theta = np.zeros((X.shape[1], 1))

    # ===================== Your Code Here =====================
    # Instructions : Complete the code to compute the closed form solution
    #                to linear regression and put the result in theta
    #

    theta = np.linalg.pinv(np.transpose(X).dot(X)).dot(np.transpose(X)).dot(y)

    return theta
