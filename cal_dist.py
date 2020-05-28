from scipy.sparse import triu
from scipy import sparse
from scipy.sparse import csr_matrix #sparse matrix
from scipy.sparse.csgraph import dijkstra
import numpy as np

def cal_dist(data):
    '''input: dataset
    ouputs: two  matricies[matricies containing distances between the graph nodes] a distance matrix
    1. of a normal sparse matrix,
    2. of a normalized t1>0 matrix '''

    T = makeMST(data)
    dimensions = T.shape #TUPLE OF DIMENSIONS (x, x)
    G = csr_matrix(T)

    T1 = T
    T1[T1 > 0] = 1  #for all T1[Elements] > 0  => 1 
    G1 = T1

    z = np.zeros(dimensions)
    z1 = np.zeros(dimensions)
    ###VISUALIZING OMIT LATER########
    plt.spy(G1)  #PLOTS SPARSE MATRICIES
    ####VISUALIZING###################
    for i in range(1, dimensions[0]):
        distmat1 = dijkstra(G, i)
        z[:] = distmat1
        distmat2 = dijkstra(G1, i)
        z1[:] = distmat2
        return z, z1
