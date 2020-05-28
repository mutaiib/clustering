from scipy.sparse import triu  #creates an upper triangluar matrix

def cciMST(data, k):
    #https://github.com/Magiccbo/CciMST/blob/master/CciMST.m
    T = makeMST(data) #GOTO makeMST.py #this creates an mst (sparse matrix)
    T1 = triu(T) #an upper triangular matrix
    T2 = T #copying data

    dist1 = cal_dist(data) #GOTO cal_dist.py

    #Determine the cluster centers
    """ TO
            RESUME
                    FROM
                            HERE
                                    """
    
