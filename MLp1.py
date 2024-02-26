from ucimlrepo import fetch_ucirepo 
import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import svd
import xlrd


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

# # basic summary statistics

# # Minimum for each feature
# print("min values:")
# print("minimum value of area:", np.min(X.Area)) # minimum value area
# print("minimum value of perimeter:", np.min(X.Perimeter)) # minimum value perimeter
# print("minimum value of MajorAxisLength:", np.min(X.MajorAxisLength)) # minimum value MajorAxisLength
# print("minimum value of MinorAxisLength:", np.min(X.MinorAxisLength)) # minimum value MinorAxisLength
# print("minimum value of eccentricity:", np.min(X.Eccentricity)) # minimum value Eccentricity
# print("minimum value of ConvexArea:", np.min(X.ConvexArea)) # minimum value ConvexArea
# print("minimum value of Extent:", np.min(X.Extent)) # minimum value Extent

# # Median for each feature
# print("median values:")
# print("median of area:", np.median(X.Area)) # median value area
# print("median of perimeter:", np.median(X.Perimeter)) # median perimeter
# print("median of MajorAxisLength:", np.median(X.MajorAxisLength)) # median MajorAxisLength
# print("median of MinorAxisLength:", np.median(X.MinorAxisLength)) # median MinorAxisLength
# print("median of eccentricity:", np.median(X.Eccentricity)) # median Eccentricity
# print("median of ConvexArea:", np.median(X.ConvexArea)) # median ConvexArea
# print("median of Extent:", np.median(X.Extent)) # median Extent

# # Maximum value for each feature
# print("max values:")
# print("max value of area:", np.max(X.Area)) # max value area
# print("max value of perimeter:", np.max(X.Perimeter)) # max value perimeter
# print("max value of MajorAxisLength:", np.max(X.MajorAxisLength)) # max value MajorAxisLength
# print("max value of MinorAxisLength:", np.max(X.MinorAxisLength)) # max value MinorAxisLength
# print("max value of eccentricity:", np.max(X.Eccentricity)) # max value Eccentricity
# print("max value of ConvexArea:", np.max(X.ConvexArea)) # max value ConvexArea
# print("max value of Extent:", np.max(X.Extent)) # max value Extent

# # mean of each feature
# print("means:")
# print("mean of area:", np.mean(X.Area)) # mean of area
# print("mean of perimeter:", np.mean(X.Perimeter)) # mean of perimeter
# print("mean of MajorAxisLength:", np.mean(X.MajorAxisLength)) # mean of MajorAxisLength
# print("mean of MinorAxisLength:", np.mean(X.MinorAxisLength)) # mean of MinorAxisLength
# print("mean of Eccentricity:", np.mean(X.Eccentricity)) # mean of Eccentricity
# print("mean of ConvexArea:", np.mean(X.ConvexArea)) # mean of ConvexArea
# print("mean of Extent:", np.mean(X.Extent)) # mean of Extent

# # standard deviation of each feature
# print("standard deviation:")
# print("standard deviation of area:", np.std(X.Area)) # standard deviation of area
# print("standard deviation of perimeter:", np.std(X.Perimeter)) # standard deviation of perimeter
# print("standard deviation of MajorAxisLength:", np.std(X.MajorAxisLength)) # standard deviation of MajorAxisLength
# print("standard deviation of MinorAxisLength:", np.std(X.MinorAxisLength)) # standard deviation of MinorAxisLength
# print("standard deviation of Eccentricity:", np.std(X.Eccentricity)) # standard deviation of Eccentricity
# print("standard deviation of ConvexArea:", np.std(X.ConvexArea)) # standard deviation of ConvexArea
# print("standard deviation of Extent:", np.std(X.Extent)) # standard deviation of Extent

# print(X.Area.size)

# statistical data visualization
# plt.boxplot(X.Area)

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

# E2.1.4
Vh = V.T
Z = Y @ Vh

i = 0
j = 1

# Plot for PC1 and PC2 (using Z) or standard scatter plot (Using X1)
plt.title("Raisin data: PCA")
for c in range(C):
    # select indices belonging to class c:
    class_mask = y == c
    plt.plot(Z[class_mask, i], Z[class_mask, j], "o", alpha=0.5)
plt.legend(classNames)
plt.xlabel("PC{0}".format(i + 1))
plt.ylabel("PC{0}".format(j + 1))


