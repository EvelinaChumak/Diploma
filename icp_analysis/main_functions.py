import open3d as o3d
import matplotlib.pyplot as plt
import numpy as np
from common.draw_result import (
    draw_registration_result,
    show_down_sample_time, 
    show_down_sample_correspondence
)
import registration
from common.transform import random_transform
from common.cloud_preparation import (
    read_clouds_source_sample, 
    read_clouds_target_sample, 
)
from time import time

trans_init = np.asarray([[1.0, 0.0, 0.0, 0.0],
                         [0.0, 1.0, 0.0, 0.0],
                         [0.0, 0.0, 1.0, 0.0], 
                         [0.0, 0.0, 0.0, 1.0]])
threshold = 0.02


def show_correspondence_down_sample_from_1_to_0_one_cloud():   
    down_sample = 1
    down_sample_array = []
    correspondence_array = []
    time_array = []
    while down_sample > 0:
        down_sample_array.append(down_sample)
        time_array_2 = []
        correspondence_array_2 = []
        for j in range (0,10):
            start_time = time()

            source, target = read_clouds_target_sample(
                down_sample, o3d.data.LivingRoomPointClouds().paths[1])
            target.transform(random_transform())

            transformation = registration.ICP_registration(
                source, target, threshold, -trans_init)
            
            correspondence_array_2.append(
                np.asarray(registration.evalution(source, target, threshold, transformation)))
            time_array_2.append(time() - start_time)
        time_array.append(np.mean(time_array_2))
        correspondence_array.append(np.mean(correspondence_array_2))

        down_sample = down_sample - 0.01

    show_down_sample_correspondence(down_sample_array, correspondence_array)
    show_down_sample_time(down_sample_array, time_array)


def show_correspondence_down_sample_from_1_to_0_ten_cloud():   
    down_sample = 1
    down_sample_array = []
    correspondence_array = []
    time_array = []
    while down_sample > 0:
        down_sample_array.append(down_sample)
        time_array_2 = []
        correspondence_array_2 = []
        for i in range(0,10): 
            time_array_3 = []
            correspondence_array_3 = []
            for j in range (0,3):
                start_time = time()

                source, target = read_clouds_target_sample(
                    down_sample, o3d.data.LivingRoomPointClouds().paths[i])
                target.transform(random_transform())

                transformation = registration.ICP_registration(
                    source, target, threshold, -trans_init)
                
                correspondence_array_3.append(
                    np.asarray(registration.evalution(source, target, threshold, transformation)))
                time_array_3.append(time() - start_time)
            correspondence_array_2.append(np.mean(correspondence_array_3))
            time_array_2.append(np.mean(time_array_3))

        time_array.append(np.mean(time_array_2))
        correspondence_array.append(np.mean(correspondence_array_2))

        down_sample = down_sample - 0.01

    show_down_sample_correspondence(down_sample_array, correspondence_array)
    show_down_sample_time(down_sample_array, time_array)


def show_correspondence_for_different_cloud():
    down_sample = 0.33
    size_1 = []
    corresponce_1 = []
    for i in range(0,57): 
        size_2 = []
        corresponce_2 = []
        for j in range (0,3): 
            source, target = read_clouds_target_sample(
                down_sample, o3d.data.LivingRoomPointClouds().paths[i])
            target.transform(random_transform())

            transformation = registration.ICP_registration(
                source, target, threshold, -trans_init)
            
            corresponce_2.append(np.asarray(
                registration.evalution(source, target, threshold, transformation)))
            size_2.append(np.asarray(source.points).size / 3)
        corresponce_1.append(np.mean(corresponce_2))
        size_1.append(np.mean(size_2))
    
    plt.scatter(size_1, corresponce_1)
    plt.xlabel('Point size')
    plt.ylabel('Correspondence')
    plt.grid(True)
    plt.show()


def show_cloud_density_and_size():
    s = []
    d = []
    for i in range(0,57):
        source, _ = read_clouds_target_sample(1, o3d.data.LivingRoomPointClouds().paths[i])
        size = np.asarray(source.points).size / 3
        s.append(size)

        neighbor_distance = np.asarray(source.compute_nearest_neighbor_distance())
        cloud_density = neighbor_distance.sum()/len(neighbor_distance)
        d.append(cloud_density)
        
    plt.scatter(s, d)
    plt.xlabel('Point size')
    plt.ylabel('Density')
    plt.grid(True)
    plt.show()
    

def show_correspondence_with_coef():
    size_1 = []
    corresponce_1 = []
    t = []
    for i in range(0,57): 
        size_2 = []
        corresponce_2 = []
        t_2 = []
        for j in range (0,3):

            neighbor_distance = np.asarray(
                source.compute_nearest_neighbor_distance())
            coeff = 0.6-(1/neighbor_distance.sum()*100)

            start_time = time()
            source, target = read_clouds_target_sample(
                coeff, o3d.data.LivingRoomPointClouds().paths[i])
            target.transform(random_transform())

            transformation = registration.ICP_registration(
                source, target, threshold, -trans_init)
            
            t_2.append((time() - start_time))
            corresponce_2.append(np.asarray(
                registration.evalution(source, target, threshold, transformation)))
            size_2.append(np.asarray(source.points).size / 3)
        corresponce_1.append(np.mean(corresponce_2))
        size_1.append(np.mean(size_2))
        t.append(np.mean(t_2))
    
    plt.scatter(size_1, corresponce_1)
    plt.xlabel('Point size')
    plt.ylabel('Correspondence')
    plt.grid(True)
    plt.show()
    plt.scatter(size_1, t)
    plt.xlabel('Point size')
    plt.ylabel('Time')
    plt.grid(True)
    plt.show()


def show_time_without_coef():
    size_1 = []
    t = []
    for i in range(0,57): 
        size_2 = []
        corresponce_2 = []
        t_2 = []
        for j in range (0,3): 
            start_time = time()

            source, target = read_clouds_target_sample(
                1, o3d.data.LivingRoomPointClouds().paths[i])
            target.transform(random_transform())

            transformation = registration.ICP_registration(
                source, target, threshold, -trans_init)
            
            corresponce_2.append(np.asarray(
                registration.evalution(source, target, threshold, transformation)))
            size_2.append(np.asarray(source.points).size / 3)
            t_2.append((time() - start_time))
        size_1.append(np.mean(size_2))
        t.append(np.mean(t_2))
    
    plt.scatter(size_1, t)
    plt.xlabel('Point size')
    plt.ylabel('Time')
    plt.grid(True)
    plt.show()


def show_correspondence_down_sample_from_1_to_0_ten_cloud_source():   
    down_sample = 1
    down_sample_array = []
    correspondence_array = []
    time_array = []
    while down_sample > 0:
        print(f"DOWN SAMPLE {down_sample}")
        down_sample_array.append(down_sample)
        time_array_2 = []
        correspondence_array_2 = []
        for i in range(0,10): 
            time_array_3 = []
            correspondence_array_3 = []
            for j in range (0,3):
                start_time = time()

                source, target = read_clouds_source_sample(
                    down_sample, o3d.data.LivingRoomPointClouds().paths[i])
                target.transform(random_transform())

                transformation = registration.ICP_registration(
                    source, target, threshold, -trans_init)
                
                correspondence_array_3.append(np.asarray(
                    registration.evalution(source, target, threshold, transformation)))

                time_array_3.append(time() - start_time)
            correspondence_array_2.append(np.mean(correspondence_array_3))
            time_array_2.append(np.mean(time_array_3))

        time_array.append(np.mean(time_array_2))
        correspondence_array.append(np.mean(correspondence_array_2))

        down_sample = down_sample - 0.1

    show_down_sample_correspondence(down_sample_array, correspondence_array)
    show_down_sample_time(down_sample_array, time_array)
