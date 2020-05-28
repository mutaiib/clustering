from scipy.spatial.distance import pdist, squareform
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import minimum_spanning_tree as krusk
 
def makeMST(data):
    '''
    input: data-set,
    ouput: a sparse matrix (MST)
    '''

    d = pdist(data, 'euclidean')
    d = squareform(d)
    xishu = csr_matrix(d)
    G = krusk(d)
    G.todense
    return G
    
####OMIT LATER#####

T = makeMST(data) #FOR TESTING
print(T) #FOR TESTING
