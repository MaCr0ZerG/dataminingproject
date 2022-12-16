import math


def kmeans(vectors: list, k=10) -> list:
    # todo: implement k-means here!

    return None


def dbscan(vectors: list, minpts: int, epsilon: float) -> list:

    # todo: implement dbscan here!
    clusters = list(list(Vector))
    for i in vectors:
        tempvectors = list(Vector)
        tempvectors[i] = Vector(i,-1,neighbours(i,vectors,epsilon))
    id = 0
    for i in tempvectors:
        if i.id == -1:
            if i.neighbours.len < minpts:
                 i.id = 0
            else:
                id += 1
                seeds = neighbours
                for j in seeds:
                    j.id = id
                seeds.remove(i)
                while seeds.len != 0:
                    k = seeds[0]
                    if k.neighbours >= minpts:
                        for l in k.neighbours:
                            if l.id < 1:
                                if l.id == -1:
                                    seeds.append(l)
                                l.id = id
                    seeds.remove(k) 
    ids = list 
    for i in tempvectors:
        ids[i] = i.id                              
    return ids

def neighbours(vector = list,vectors = list, epsilon = float) -> list:
    neighbours = list
    for i in vectors:
        if distance(vector, i) <= epsilon:
            neighbours.append(i)
    return neighbours

def distance(vector1: list, vector2: list ) -> float:

    # distance between two n-dimensional points.
    distance = float
    for i in vector1.count:
        distance += (vector1[i] - vector2[i])^2
    
    distance = math.sqrt(distance)
    return distance

class Vector :
    def __init__(self, list, id, neighbours):
        self.list = list
        self.id = id
        self.neighbours = neighbours
