
import pandas as pd
import numpy as np
import re
import matplotlib.patches as mpatches
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib as mpl
from sklearn.decomposition import KernelPCA
from movement import Movement


def kpca(arr):
    kernel_pca = KernelPCA(kernel="rbf", fit_inverse_transform=True, gamma=10)
    X_kernel_pca = kernel_pca.fit_transform(arr)
    return arr

m = Movement(3,10,18,12)
m.readFromCsv("datasetbis.csv")
m.saveFigSensorsByMovements()
#m.dimensionReduction(1,2)
m.describe()