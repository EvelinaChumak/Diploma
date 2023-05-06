import open3d as o3d
import numpy as np
from time import time

from common.draw_result import show_down_sample_correspondese, show_down_sample_time
from common.cloud_preparation import read_clouds_source_sample, read_clouds_target_sample, read_clouds_voxel_sample
from ransac_analysis.registration import execute_global_registration_with_target_density
from common.transform import random_transform


trans_init = np.asarray([[1.0, 0.0, 0.0, 0.0],
                         [0.0, 1.0, 0.0, 0.0],
                         [0.0, 0.0, 1.0, 0.0], 
                         [0.0, 0.0, 0.0, 1.0]])
    
def show_correspondese_down_sample_from_1_to_0_ten_cloud_target():   
    down_sample = 1
    down_sample_array = []
    correspondese_array = []
    time_array = []
    while down_sample > 0:
        down_sample_array.append(down_sample)
        time_array_2 = []
        correspondese_array_2 = []
        for i in range(0,10): 
            start_time = time()
            source, target = read_clouds_target_sample(down_sample, o3d.data.LivingRoomPointClouds().paths[i])
            target.transform(random_transform(low=100, high=100, rotation=180)) 
            result = execute_global_registration_with_target_density(source, target)
            print(result)
            correspondese_array_2.append(np.asarray(result.fitness))
            time_array_2.append(time() - start_time)
            print(time_array_2)
            print(down_sample)


        time_array.append(np.mean(time_array_2))
        correspondese_array.append(np.mean(correspondese_array_2))

        down_sample = down_sample - 0.02

    show_down_sample_correspondese(down_sample_array, correspondese_array)
    show_down_sample_time(down_sample_array, time_array)



def show_correspondese_down_sample_from_1_to_0_ten_cloud_source():   
    down_sample = 1
    down_sample_array = []
    correspondese_array = []
    time_array = []
    while down_sample > 0:
        down_sample_array.append(down_sample)
        time_array_2 = []
        correspondese_array_2 = []
        for i in range(0,10): 
            start_time = time()
            source, target = read_clouds_source_sample(down_sample, o3d.data.LivingRoomPointClouds().paths[i])
            target.transform(random_transform(low=100, high=100, rotation=180)) 
            result = execute_global_registration_with_target_density(source, target)
            print(result)
            correspondese_array_2.append(np.asarray(result.fitness))
            time_array_2.append(time() - start_time)
            print(time_array_2)
            print(down_sample)


        time_array.append(np.mean(time_array_2))
        correspondese_array.append(np.mean(correspondese_array_2))

        down_sample = down_sample - 0.02

    show_down_sample_correspondese(down_sample_array, correspondese_array)
    show_down_sample_time(down_sample_array, time_array)


def show_correspondese_down_sample_from_1_to_0_ten_cloud():   
    down_sample = 1
    down_sample_array = []
    correspondese_array = []
    time_array = []
    while down_sample > 0:
        down_sample_array.append(down_sample)
        time_array_2 = []
        correspondese_array_2 = []
        for i in range(0,10): 
            start_time = time()
            source_s, target = read_clouds_target_sample(down_sample, o3d.data.LivingRoomPointClouds().paths[i])
            source, target_s = read_clouds_source_sample(down_sample, o3d.data.LivingRoomPointClouds().paths[i])
            target.transform(random_transform(low=100, high=100, rotation=180)) 
            result = execute_global_registration_with_target_density(source, target)
            print(result)
            correspondese_array_2.append(np.asarray(result.fitness))
            time_array_2.append(time() - start_time)
            print(time_array_2)
            print(down_sample)


        time_array.append(np.mean(time_array_2))
        correspondese_array.append(np.mean(correspondese_array_2))

        down_sample = down_sample - 0.02

    show_down_sample_correspondese(down_sample_array, correspondese_array)
    show_down_sample_time(down_sample_array, time_array)


def show_correspondese_voxel_down_sample_from_1_to_0_one_cloud():   
    down_sample = 1
    down_sample_array = []
    correspondese_array = []
    time_array = []
    while down_sample >= 0.05:
        down_sample_array.append(down_sample)
        time_array_2 = []
        correspondese_array_2 = []
        for i in range(0,3): 
            start_time = time()
            source, target = read_clouds_voxel_sample(down_sample, o3d.data.LivingRoomPointClouds().paths[1])
            target.transform(random_transform(low=0.1, high=0.1, rotation=180)) 
            result = execute_global_registration_with_target_density(source, target)
            print(result)
            correspondese_array_2.append(np.asarray(result.fitness))
            time_array_2.append(time() - start_time)
            print(time_array_2)
            print(down_sample)


        time_array.append(np.mean(time_array_2))
        correspondese_array.append(np.mean(correspondese_array_2))

        down_sample = down_sample - 0.05

    show_down_sample_correspondese(down_sample_array, correspondese_array)
    show_down_sample_time(down_sample_array, time_array)

def show_correspondese_voxel_down_sample_from_1_to_0_ten_cloud():   
    down_sample = 1
    down_sample_array = []
    correspondese_array = []
    time_array = []
    while down_sample >= 0.02:
        down_sample_array.append(down_sample)
        time_array_2 = []
        correspondese_array_2 = []
        for i in range(0,10): 
            start_time = time()
            source, target = read_clouds_voxel_sample(down_sample, o3d.data.LivingRoomPointClouds().paths[i])
            target.transform(random_transform(low=100, high=100, rotation=180)) 
            result = execute_global_registration_with_target_density(source, target)
            print(result)
            correspondese_array_2.append(np.asarray(result.fitness))
            time_array_2.append(time() - start_time)
            print(time_array_2)
            print(down_sample)


        time_array.append(np.mean(time_array_2))
        correspondese_array.append(np.mean(correspondese_array_2))

        down_sample = down_sample - 0.02

    show_down_sample_correspondese(down_sample_array, correspondese_array)
    show_down_sample_time(down_sample_array, time_array)
