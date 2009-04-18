from numpy import *
import heapq
from collections import defaultdict

adjacentIndexOffsets = ((-1,1),(-1,-1),(1,-1),(1,1))

def dijkstra(seedImage):
    """
    Returns the distance to every vertex from the source and the
    array representing, at index i, the node visited before
    visiting node i. This is in the form (dist, previous).
    """
    distanceDataType = float
    NOT_VISITED = finfo(distanceDataType).max
    distanceImage = zeros(seedImage.shape, dtype=distanceDataType)
    distanceImage[:,:] = NOT_VISITED

    visited, queue = {}, []
    for i in range(seedImage.shape[0]):
        for j in range(seedImage.shape[1]):
            if seedImage[i,j]:
                distanceImage[i,j] = 0
                heapq.heappush(queue, (0, (i,j)))

        
        
 
            if adjacentI >= 0 and adjacentI < seedImage.shape[0] and adjacentJ >= 0 and adjacentJ < seedImage.shape[1]:


    