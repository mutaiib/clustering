from scipy.io import loadmat
import numpy as np

#LOADING THE DATASET
data = loadmat('WheatSeeds.mat')
group = loadmat('WheatSeedsgroup.mat')

#TRANSFORMING DATA SET INTO A NUMPY ARRAY
data = np.copy(data['data'])
group = np.copy(group['group'])

#K = NUMBER OF CLUSTERS, np.unique creates a unique (union) array of elements.
k = len(np.unique(group))
print(k)
clusterLabel, center = cciMST(data, K); #GOTO cciMST.py

#THIS CODE IS NOT COMPLETE
