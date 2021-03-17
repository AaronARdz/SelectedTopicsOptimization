import numpy as np
import copy
# steps :
# 1. Initialize all vertices as unvisited.
# 2. Select an arbitrary vertex, set it as the current vertex u. Mark u as visited.
# 3. Find out the shortest edge connecting the current vertex u and an unvisited vertex v.
# 4. Set v as the current vertex u. Mark v as visited.
# 5. If all the vertices in the domain are visited, then terminate. Else, go to step 3.

# Expected order is 0,2,3,1,4

def NN(A, start):
    """Nearest neighbor algorithm.
    A is an NxN array indicating distance between N locations
    start is the index of the starting location
    Returns the path and cost of the found solution
    """
    path = [start]
    cost = 0
    N = A.shape[0]
    mask = np.ones(N, dtype=bool)  # boolean values indicating which
                                   # locations have not been visited
    print(mask)
    mask[start] = False

    for i in range(N-1):
        last = path[-1]
        next_ind = np.argmin(A[last][mask]) # find minimum of remaining locations
        next_loc = np.arange(N)[mask][next_ind] # convert to original location
        path.append(next_loc)
        mask[next_loc] = False
        cost += A[last, next_loc]

    return path, cost


A = np.array([
    [0, 2, 1, 2, 2],
    [2, 0, 2, 1, 1],
    [1, 2, 0, 1, 2],
    [2, 1, 1, 0, 2],
    [2, 1, 2, 2, 0]])


print(NN(A,0))