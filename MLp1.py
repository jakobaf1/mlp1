from ucimlrepo import fetch_ucirepo 
import numpy as np
  
# fetch dataset 
raisin = fetch_ucirepo(id=850) 
  
# data (as pandas dataframes) 
X = raisin.data.features 
y = raisin.data.targets 
  
# metadata 
print(raisin.metadata) 
  
# variable information 
print(raisin.variables)

# basic summary statistics

# Minimum for each feature
print("min values:")
print("minimum value of area:", np.min(X.Area)) # minimum value area
print("minimum value of perimeter:", np.min(X.Perimeter)) # minimum value perimeter
print("minimum value of MajorAxisLength:", np.min(X.MajorAxisLength)) # minimum value MajorAxisLength
print("minimum value of MinorAxisLength:", np.min(X.MinorAxisLength)) # minimum value MinorAxisLength
print("minimum value of eccentricity:", np.min(X.Eccentricity)) # minimum value Eccentricity
print("minimum value of ConvexArea:", np.min(X.ConvexArea)) # minimum value ConvexArea
print("minimum value of Extent:", np.min(X.Extent)) # minimum value Extent

# Median for each feature
print("median values:")
print("median of area:", np.median(X.Area)) # median value area
print("median of perimeter:", np.median(X.Perimeter)) # median perimeter
print("median of MajorAxisLength:", np.median(X.MajorAxisLength)) # median MajorAxisLength
print("median of MinorAxisLength:", np.median(X.MinorAxisLength)) # median MinorAxisLength
print("median of eccentricity:", np.median(X.Eccentricity)) # median Eccentricity
print("median of ConvexArea:", np.median(X.ConvexArea)) # median ConvexArea
print("median of Extent:", np.median(X.Extent)) # median Extent

# Maximum value for each feature
print("max values:")
print("max value of area:", np.max(X.Area)) # max value area
print("max value of perimeter:", np.max(X.Perimeter)) # max value perimeter
print("max value of MajorAxisLength:", np.max(X.MajorAxisLength)) # max value MajorAxisLength
print("max value of MinorAxisLength:", np.max(X.MinorAxisLength)) # max value MinorAxisLength
print("max value of eccentricity:", np.max(X.Eccentricity)) # max value Eccentricity
print("max value of ConvexArea:", np.max(X.ConvexArea)) # max value ConvexArea
print("max value of Extent:", np.max(X.Extent)) # max value Extent

# mean of each feature
print("means:")
print("mean of area:", np.mean(X.Area)) # mean of area
print("mean of perimeter:", np.mean(X.Perimeter)) # mean of perimeter
print("mean of MajorAxisLength:", np.mean(X.MajorAxisLength)) # mean of MajorAxisLength
print("mean of MinorAxisLength:", np.mean(X.MinorAxisLength)) # mean of MinorAxisLength
print("mean of Eccentricity:", np.mean(X.Eccentricity)) # mean of Eccentricity
print("mean of ConvexArea:", np.mean(X.ConvexArea)) # mean of ConvexArea
print("mean of Extent:", np.mean(X.Extent)) # mean of Extent

# standard deviation of each feature
print("standard deviation:")
print("standard deviation of area:", np.std(X.Area)) # standard deviation of area
print("standard deviation of perimeter:", np.std(X.Perimeter)) # standard deviation of perimeter
print("standard deviation of MajorAxisLength:", np.std(X.MajorAxisLength)) # standard deviation of MajorAxisLength
print("standard deviation of MinorAxisLength:", np.std(X.MinorAxisLength)) # standard deviation of MinorAxisLength
print("standard deviation of Eccentricity:", np.std(X.Eccentricity)) # standard deviation of Eccentricity
print("standard deviation of ConvexArea:", np.std(X.ConvexArea)) # standard deviation of ConvexArea
print("standard deviation of Extent:", np.std(X.Extent)) # standard deviation of Extent


