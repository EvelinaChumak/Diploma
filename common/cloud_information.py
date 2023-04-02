import numpy as np


def cloud_size(cloud):
    size = np.asarray(cloud.points).size / 3
    return size


def cloud_density(cloud):
    neighbor_distance = np.asarray(cloud.compute_nearest_neighbor_distance())
    density = neighbor_distance.sum()/len(neighbor_distance)
    return density
