import open3d as o3d
import numpy as np

from common.cloud_preparation import read_clouds_target_sample
from common.transform import random_transform
from icp_analysis.registration import evalution

trans_init = np.asarray([[1.0, 0.0, 0.0, 0.0],
                         [0.0, 1.0, 0.0, 0.0],
                         [0.0, 0.0, 1.0, 0.0], 
                         [0.0, 0.0, 0.0, 1.0]])
threshold = 0.02

def valid_correspondence():
    correspondese_array = []
    for i in range(0,57): 
        correspondese_array_2 = []
        for j in range(0,5):
            source, target = read_clouds_target_sample(1, o3d.data.LivingRoomPointClouds().paths[i])
            target.transform(random_transform()) 
            correspondese_array_2.append(np.asarray(evalution(source, target, threshold, trans_init)))
        correspondese_array.append(np.mean(correspondese_array_2))

    print (np.mean(correspondese_array))
    