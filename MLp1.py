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

# translating data to matrix format
X = np.empty((N, 7))
X[:,0] = np.asarray(X1.Area)
X[:,1] = np.asarray(X1.MajorAxisLength)
X[:,2] = np.asarray(X1.MinorAxisLength)
X[:,3] = np.asarray(X1.Eccentricity)
X[:,4] = np.asarray(X1.ConvexArea)
X[:,5] = np.asarray(X1.Extent)
X[:,6] = np.asarray(X1.Perimeter)

# We standardize the data since we have very different scales in our data
Y = (X - np.ones((N, 1))*X.mean(axis=0))*1/X.std(axis=0)

# We get the PCA using svd of Y
U, S, V = svd(Y, full_matrices=False)

# Array with variances for each PC
rho = (S * S) / (S * S).sum()
print(rho)
# Contribution of each parameter to PC1
print(V[0])
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

# Plot for PC(i+1) and PC(j+1)
plt.title("Raisin data: PCA")
for c in range(C):
    # select indices belonging to class c:
    class_mask = y == c
    plt.plot(Z[class_mask, i], Z[class_mask, j], "o", alpha=0.5)
plt.legend(classNames)
plt.xlabel("PC{0}".format(i + 1))
plt.ylabel("PC{0}".format(j + 1))
plt.show()

# Plot visualising feature coefficients for PCs
N, M = X.shape
pcs = [0, 1, 2]
legendStrs = ["PC" + str(e + 1) for e in pcs]
c = ["r", "g", "b"]
bw = 0.2
r = np.arange(1, M + 1)
for i in pcs:
    plt.bar(r + i * bw, Vh[:, i], width=bw)
plt.xticks(r + bw, ["Area", "MajorAxisLength", "MinorAxisLength", "Eccentricity", "ConvexArea", "Extent", "Perimeter"])
plt.xlabel("Attributes")
plt.ylabel("Component coefficients")
plt.legend(legendStrs)
plt.grid()
plt.title("PCA Component Coefficients")
plt.show()


