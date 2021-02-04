"""
https://github.com/PacktPublishing/Python-Machine-Learning-Cookbook/tree/master/Chapter10
"""

import numpy as np
import pandas as pd
import re
import matplotlib.pyplot as plt
from sklearn.decomposition import KernelPCA
from sklearn.datasets import make_circles
import csv

################################################################################
def kpca(arr):
    kernel_pca = KernelPCA(kernel="rbf", fit_inverse_transform=True, gamma=10)
    X_kernel_pca = kernel_pca.fit_transform(arr)

    # Plot original data
    plt.figure()
    plt.title("Original data")
    for ele in arr :
        plt.plot(ele[0], ele[1], "ko", mfc='none')

    plt.xlabel("1st dimension")
    plt.ylabel("2nd dimension")

    # Plot Kernel PCA projection of the data
    plt.figure()
    for ele in arr :
        plt.plot(X_kernel_pca[0], X_kernel_pca[1], "ko", mfc='none')
    plt.title("Data transformed using Kernel PCA")
    plt.xlabel("1st principal component")
    plt.ylabel("2nd principal component")

    plt.show()
################################################################################
def readCsvSimulation():
    data = pd.read_csv("dataset.csv")
    arr = np.zeros((10000,2))
    i = 0
    for el in data :
        num = re.findall(r'\d+',str(el))
        arr[int(i/2)][i%2] = num[0]
        i = i+1
    return arr
################################################################################
kpca(readCsvSimulation())


