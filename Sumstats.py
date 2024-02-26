from MLp1 import *

# basic summary statistics

# Minimum for each feature
print("min values:")
print("minimum value of area:", np.min(X1.Area)) # minimum value area
print("minimum value of perimeter:", np.min(X1.Perimeter)) # minimum value perimeter
print("minimum value of MajorAxisLength:", np.min(X1.MajorAxisLength)) # minimum value MajorAxisLength
print("minimum value of MinorAxisLength:", np.min(X1.MinorAxisLength)) # minimum value MinorAxisLength
print("minimum value of eccentricity:", np.min(X1.Eccentricity)) # minimum value Eccentricity
print("minimum value of ConvexArea:", np.min(X1.ConvexArea)) # minimum value ConvexArea
print("minimum value of Extent:", np.min(X1.Extent)) # minimum value Extent

# Median for each feature
print("median values:")
print("median of area:", np.median(X1.Area)) # median value area
print("median of perimeter:", np.median(X1.Perimeter)) # median perimeter
print("median of MajorAxisLength:", np.median(X1.MajorAxisLength)) # median MajorAxisLength
print("median of MinorAxisLength:", np.median(X1.MinorAxisLength)) # median MinorAxisLength
print("median of eccentricity:", np.median(X1.Eccentricity)) # median Eccentricity
print("median of ConvexArea:", np.median(X1.ConvexArea)) # median ConvexArea
print("median of Extent:", np.median(X1.Extent)) # median Extent

# Maximum value for each feature
print("max values:")
print("max value of area:", np.max(X1.Area)) # max value area
print("max value of perimeter:", np.max(X1.Perimeter)) # max value perimeter
print("max value of MajorAxisLength:", np.max(X1.MajorAxisLength)) # max value MajorAxisLength
print("max value of MinorAxisLength:", np.max(X1.MinorAxisLength)) # max value MinorAxisLength
print("max value of eccentricity:", np.max(X1.Eccentricity)) # max value Eccentricity
print("max value of ConvexArea:", np.max(X1.ConvexArea)) # max value ConvexArea
print("max value of Extent:", np.max(X1.Extent)) # max value Extent

# mean of each feature
print("means:")
print("mean of area:", np.mean(X1.Area)) # mean of area
print("mean of perimeter:", np.mean(X1.Perimeter)) # mean of perimeter
print("mean of MajorAxisLength:", np.mean(X1.MajorAxisLength)) # mean of MajorAxisLength
print("mean of MinorAxisLength:", np.mean(X1.MinorAxisLength)) # mean of MinorAxisLength
print("mean of Eccentricity:", np.mean(X1.Eccentricity)) # mean of Eccentricity
print("mean of ConvexArea:", np.mean(X1.ConvexArea)) # mean of ConvexArea
print("mean of Extent:", np.mean(X1.Extent)) # mean of Extent

# standard deviation of each feature
print("standard deviation:")
print("standard deviation of area:", np.std(X1.Area)) # standard deviation of area
print("standard deviation of perimeter:", np.std(X1.Perimeter)) # standard deviation of perimeter
print("standard deviation of MajorAxisLength:", np.std(X1.MajorAxisLength)) # standard deviation of MajorAxisLength
print("standard deviation of MinorAxisLength:", np.std(X1.MinorAxisLength)) # standard deviation of MinorAxisLength
print("standard deviation of Eccentricity:", np.std(X1.Eccentricity)) # standard deviation of Eccentricity
print("standard deviation of ConvexArea:", np.std(X1.ConvexArea)) # standard deviation of ConvexArea
print("standard deviation of Extent:", np.std(X1.Extent)) # standard deviation of Extent

print(X1.Area.size)

# statistical data visualization
# Scatter plots:
plt.figure()
plt.plot(X[:,0], X[:, 4], "o", alpha=0.5)
plt.title("Scatterplot of Area and ConvexArea")
plt.xlabel("Area")
plt.ylabel("ConvexArea")
plt.show()

plt.figure()
plt.plot(X[:,0], X[:, 6], "o", alpha=0.5)
plt.title("Scatterplot of Eccentricity and Extent")
plt.xlabel("Area")
plt.ylabel("Perimeter")
plt.show()

# Boxplots:
data1 = [X[:,0], X[:,4]]
plt.figure()
plt.boxplot(data1)
plt.title("Boxplot of Area and ConvexArea")
plt.show()

data2 = [X[:,3], X[:,5]]
plt.figure()
plt.boxplot(data2)
plt.title("Boxplot of Eccentricity and extent")
plt.show()

# Histograms:
plt.figure()
plt.hist(X[:,0])
plt.title("Histogram of Area")
plt.ylabel("Area")
plt.show()

# Normal Distributions:
mean = np.mean(X[:,0])
std = np.std(X[:,0])
print(np.mean(X[:,0]))
x = np.arange(mean-3*std, mean+3*std, 1)
plt.figure()
plt.plot(x, stats.norm.pdf(x, mean, std))
plt.title("Normal distribution of Area")
plt.ylabel("percentile x 10^(-5)")
plt.xlabel("Area")
plt.show()