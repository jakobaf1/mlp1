from ucimlrepo import fetch_ucirepo 
import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import svd
import scipy.stats as stats

# fetch dataset 
raisin = fetch_ucirepo(id=850) 

# data (as pandas dataframes) 
X1 = raisin.data.features 
y = raisin.data.targets 
N = X1.Area.size

classLabels = np.asarray(y.Class)
classNames = sorted(set(classLabels))
classDict = dict(zip(classNames, range(2)))

y = np.asarray([classDict[value] for value in classLabels])


C = len(classNames)
  
# metadata 
# print(raisin.metadata) 
  
# # variable information 
# print(raisin.variables)

# translating data to matrix format
X = np.empty((N, 7))
X[:,0] = np.asarray(X1.Area)
X[:,1] = np.asarray(X1.MajorAxisLength)
X[:,2] = np.asarray(X1.MinorAxisLength)
X[:,3] = np.asarray(X1.Eccentricity)
X[:,4] = np.asarray(X1.ConvexArea)
X[:,5] = np.asarray(X1.Extent)
X[:,6] = np.asarray(X1.Perimeter)

Y = X - np.ones((N, 1))*X.mean(axis=0)

U, S, V = svd(Y, full_matrices=False)

# Array with variances for each PC
rho = (S * S) / (S * S).sum()
# print(rho)

# Plot variance explained
plt.figure()
plt.plot(range(1, len(rho) + 1), rho, "x-")
plt.plot(range(1, len(rho) + 1), np.cumsum(rho), "o-")
plt.title("Variance explained by principal components")
plt.xlabel("Principal component")
plt.ylabel("Variance explained")
plt.legend(["Individual", "Cumulative"])
plt.grid()
plt.show()

# Plotting with Principal components
Vh = V.T
Z = Y @ Vh

i = 0
j = 1

# Plot for PC1 and PC2 (using Z) or standard scatter plot (Using X)
plt.title("Raisin data: PCA")
for c in range(C):
    # select indices belonging to class c:
    class_mask = y == c
    plt.plot(Z[class_mask, i], Z[class_mask, j], "o", alpha=0.5)
plt.legend(classNames)
plt.xlabel("PC{0}".format(i + 1))
plt.ylabel("PC{0}".format(j + 1))


