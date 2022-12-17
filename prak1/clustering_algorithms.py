
import random
import math

def kmeans(vectors: list, k=10) -> list:
    # init
    randomMeanList = random.sample(range(0, len(vectors) - 1), k)

    means = []
    for m in randomMeanList:
        means.append(vectors[m])

    # assign
    clusterOldList = [] # list of num of cluster the vector in that spot is in
    while True: 

        clusterNewList = []
        smallestVar = 9999999
        smallestVarIndex = 0
        varNew = 0
        
        for vector in vectors:
            i = 0
            varNewVec = [0, 0, 0]

            for m in means:
                varIndexNew = i
                varNewVec[0] = vector[0] - means[i][0] 
                varNewVec[1] = vector[1] - means[i][1]
                varNewVec[2] = vector[2] - means[i][2]
                
                
                sq = math.sqrt( float( (varNewVec[0] ** 2) + (varNewVec[1] ** 2) + (varNewVec[2] ** 2) ))
                varNew = sq # compute distance of vector to mean
                

                if i == 0:
                    smallestVar = varNew
                    smallestVarIndex = varIndexNew

                if varNew < smallestVar:
                    smallestVar = varNew
                    smallestVarIndex = varIndexNew

                i = i + 1

            clusterNewList.append(smallestVarIndex)

        if clusterNewList == clusterOldList: # no change -> break
            break

        clusterOldList = clusterNewList
        # update means
        means = [[0,0,0] , [0,0,0] , [0,0,0] , [0,0,0]]
        clustercount = [0, 0, 0, 0] 

        for num in clusterNewList:
            means[num][0] = means[num][0] + vectors[num][0] # sum of vectors in cluster
            means[num][1] = means[num][1] + vectors[num][1]
            means[num][2] = means[num][2] + vectors[num][2]
            clustercount[num] = clustercount[num] + 1 # num of vectors in cluster

        for n in range(0, k):
            means[n][0] = int(means[n][0] / clustercount[n])
            means[n][1] = int(means[n][1] / clustercount[n])
            means[n][2] = int(means[n][2] / clustercount[n])

    return clusterNewList


def dbscan(vectors: list, minpts: int, epsilon: int) -> list:
    # todo: implement k-means here!

    return None
