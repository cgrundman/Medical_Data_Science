#######################################################################################################################
# Implementation of a k-means algorithm.
# 
# Pseudo-code:
# 1 - Initialise k cluster centers at random
# 2 - While no convergence
#      Attibute every point of the dataset to a cluster based on its distance to the centers
#      Compute the new cluster centers
# 3 - Return cluster centers
#######################################################################################################################

import numpy as np
import matplotlib.pyplot as plt

from pdb import set_trace as st

#######################################################################################################################
# Function initialiseCenters(k,d,minList,maxList)
# Return the coordinates of k cluster centers initlialised at random in a space of dimension d.
# 
# Input arguments:
#    - [int] k: number of clusters.
#    - [int] d: dimension of the data space.
#    - [list] minList: minimum values for the random initialisation of each coordinate. Must have a length of d. 
#    - [list] maxList: maximum values for the random initialisation of each coordinate. Must have a length of d. 
#
# Output argument:
#    - [array] output: array of dimension k x d containing the coordinates of the initial cluster centers.
#######################################################################################################################
def initialiseCenters(k,d,minList,maxList):
    ### TODO: complete
    return

#######################################################################################################################
# Function checkConvergence(oldCenters,newCenters,epsilon=1e-5)
# Check if the distance between the old and new cluster centers is small enough to consider convergence.
#
# Input arguments:
#    - [array] oldCenters: array of dimension k x d containing the coordinates of the previous cluster centers.
#    - [array] newCenters: array of dimension k x d containing the coordinates of the new cluster centers.
#    - [float] epsilon: distance threshold under which convergence is considered (default: 1e-5)
#
# Output argument:
#    - [bool] output: True if convergence, False otherwise
#######################################################################################################################
def checkConvergence(oldCenters,newCenters,epsilon=1e-5):
    ### TODO: complete
    return

#######################################################################################################################
# Function attributeCluster(dataset,clusterCenters)
# Attribute every point of a dataset to the closest cluster center. 
#
# Input arguments:
#    - [array] dataset: array of dimension nbExamples x d containing the data to be clustered.
#    - [array] clusterCenters: array of dimension k x d containing the coordinates of the cluster centers.
#
# Output argument:
#    - [array] output: array of dimension nbExamples x 1 containing the cluster IDs (integer between 0 and k-1)
#       corresponding to each data point of dataset.
#######################################################################################################################
def attributeCluster(dataset,clusterCenters):
    ### TODO: complete
    return

#######################################################################################################################
# Function computeNewCenters(dataset,clusterLabels,k)
# Compute the new clusters given a cluster association vector and a dataset. 
#
# Input arguments:
#    - [array] dataset: array of dimension nbExamples x d containing the data to be clustered.
#    - [array] clusterLabels: array of dimension nbExamples x 1 containing the cluster IDs (integer between 0 and k-1)
#       corresponding to each data point of dataset.
#    - [int] k: number of clusters
#
# Output argument:
#    - [array] output: array of dimension k x d containing the coordinates of the new cluster centers.
#######################################################################################################################
def computeNewCenters(dataset,clusterLabels,k):
    ### TODO: complete
    return

#######################################################################################################################
# Function generateRandom2DNormalData(nbPoints,d,mean,covariance)
# Generate random 2D data points following normal distributions given Gaussian parameters.  
#
# Input arguments:
#    - [int] nbPoints: number of random points to generate.
#    - [array] mean: array of size 2 x 1 containing the coordinates of the gaussian mean.
#    - [array] covariance: array of size 2 x 2 containing the covarainces of the gaussian.
#
# Output argument:
#    - [array] output: array of dimension nbPoints x 2 containing random data points following a Gaussian distribution.
#######################################################################################################################
def generateRandom2DNormalData(nbPoints,mean,covariance):
    # Check if the dimensions are consistent
    d = mean.shape[0]
    assert covariance.shape == (d,d)
    # Initlialise result array
    randomData = np.zeros((nbPoints,d),dtype=np.float32)
    # Generate the random data points
    for exampleIdx in range(nbPoints):
        randomData[exampleIdx] = np.random.multivariate_normal(mean,covariance)
    return randomData


#######################################################################################################################
# Main function
# NOTE: the following script only works for dimension = 2 due to the plotting of 2D graphs
#######################################################################################################################
if __name__ == "__main__":
    
    ### Hyper parameters
    k = 3 #  Number of clusters
    d = 2 # Number of dimension (keep equal to 2 for this script)
    nbExamplesPerCluster = 25 # Number of examples per cluster
    maxIterations = 20 # Maximum number of iterations for the k-means clustering to converge
    displayOn = True # Enable or disable plotting after each iteration

    # Dictionary containing 2D Gaussian parameters for the random data generation.
    # Dictionary values are under the format (meanVector,convarianceMatrix)
    # NOTE: change this to obtain different clusters
    gaussianParams = {
        0: (np.array([1,3]),np.array([[2,0],[0,2]])),
        1: (np.array([-6,-3]),np.array([[2,0],[0,2]])),
        2: (np.array([2,-3]),np.array([[2,0],[0,2]])),
    }

    ### Random data generation following k multivariate Gaussians
    print('Generating %d random data points ...' % (k*nbExamplesPerCluster))

    dataDictionary = {}
    for clusterIdx in range(len(gaussianParams.keys())):
        dataDictionary[clusterIdx] = generateRandom2DNormalData(nbExamplesPerCluster,gaussianParams[clusterIdx][0],gaussianParams[clusterIdx][1])

    fullDataset = np.vstack(dataDictionary.values()) # Concatenation of all data points

    ### Plotting the data
    plt.grid()
    plt.scatter(fullDataset[:,0],fullDataset[:,1],marker='*',c='k')

    ### Initialise k cluster centers
    initialCenters = initialiseCenters(k,d,np.amin(fullDataset,axis=0),np.amax(fullDataset,axis=0))
    plt.scatter(initialCenters[:,0],initialCenters[:,1],marker='o',c='r',edgecolors='k')
    plt.suptitle('Initial configuration')
    plt.suptitle('Black: data points | Red: cluster center')
    plt.draw()
    plt.pause(0.3)
    input('Press a key to continue ...')
    plt.close()

    ### Start the k-means clustering
    convergence = False
    nbIterations = 0
    currentCenters = initialCenters
    previousCenters = [initialCenters] # For display purposes
    colors = ['b','g','m','c','k','orange','lightcoral','darkturquoise','slategray','wheat','orchid','navy','salmon']

    while not convergence and nbIterations < maxIterations:
        # Attribute each point of the dataset to a cluster center
        clusterLabels = attributeCluster(fullDataset,currentCenters)
        # Compute new cluster centers
        newCenters = computeNewCenters(fullDataset,clusterLabels,k)
        # Check for convergence
        convergence = checkConvergence(currentCenters,newCenters)
        # Iterate
        nbIterations += 1
        currentCenters = newCenters
        previousCenters += [currentCenters]
        # Plot current configuration
        if displayOn:
            plt.grid()
            plt.scatter(currentCenters[:,0],currentCenters[:,1],marker='o',c='r',edgecolors='k') # Plot current cluster centers
            for idx in range(k): # Attribute colors to current clusters
                plt.scatter(fullDataset[clusterLabels==idx,0],fullDataset[clusterLabels==idx,1],marker='*',c=colors[idx%len(colors)])
            for idx in range(len(previousCenters)): # Plot previous cluster centers
                plt.scatter(previousCenters[idx][:,0],previousCenters[idx][:,1],marker='o',c='r',alpha=0.25)
            plt.title('k-means clustering after iteration %d' % (nbIterations))
            plt.draw()
            plt.pause(0.3)
            input('Press a key to continue ...')
            plt.close()

    if convergence:
        print('Convergence reached after iteration %d.' % (nbIterations))
    else:
        print('Maximum number of iteration reached!')

    ### Plot final configuration
    plt.grid()
    plt.scatter(currentCenters[:,0],currentCenters[:,1],marker='o',c='r',edgecolors='k') # Plot final cluster centers
    for idx in range(k): # Attribute colors to current clusters
        plt.scatter(fullDataset[clusterLabels==idx,0],fullDataset[clusterLabels==idx,1],marker='*',c=colors[idx%len(colors)])
    for idx in range(len(previousCenters)): # Plot previous cluster centers
        plt.scatter(previousCenters[idx][:,0],previousCenters[idx][:,1],marker='o',c='r',alpha=0.25)
    plt.title('k-means clustering after convergence')
    plt.draw()
    plt.pause(0.3)
    input('Press a key to continue ...')
    plt.close()

    ### Print new cluster coordinates
    print('New cluster centers coordinates:')
    for idx in range(k):
        print('    %d - (%.2f,%.2f)' % (idx+1,currentCenters[idx,0],currentCenters[idx,1]))