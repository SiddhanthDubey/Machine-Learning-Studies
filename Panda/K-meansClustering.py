import random


def createClusterData(N,k):
    random.seed(10)
    pointsPerCluster = float(N)/k
    X = []

