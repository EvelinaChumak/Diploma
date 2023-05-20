import open3d as o3d
import numpy as np
from time import time

from common.draw_result import (
    show_down_sample_correspondence, 
    show_down_sample_time, 
    draw_registration_result
)
from common.cloud_preparation import (
    read_clouds, 
    read_clouds_voxel_sample_from_documentation
)
from common.cloud_preparation import (
    read_cloud_voxel_sample_different_cloud, 
    read_clouds_target_sample
)
from ransac_analysis.registration import execute_global_registration_with_target_density
from icp_analysis import registration

trans_init = np.asarray([[1.0, 0.0, 0.0, 0.0],
                         [0.0, 1.0, 0.0, 0.0],
                         [0.0, 0.0, 1.0, 0.0], 
                         [0.0, 0.0, 0.0, 1.0]])

source_path = o3d.data.DemoICPPointClouds().paths[0]
target_path = o3d.data.DemoICPPointClouds().paths[1]
threshold = 0.02


def result_from_documentstion():
    t = []
    for i in range(0, 10):
        source, target = read_clouds(source_path, target_path)
        #draw_registration_result(source, target, trans_init)
        start_time = time()
        source_ransac, target_ransac = read_clouds_voxel_sample_from_documentation(
            source_path, target_path)
        
        result = execute_global_registration_with_target_density(
            source_ransac, target_ransac)
        #draw_registration_result(source, target, result.transformation)
        source.transform(result.transformation)

        transformation = registration.ICP_registration(
            source, target, threshold, -trans_init)
        
        end_time = time()
        t.append(end_time-start_time)
        #draw_registration_result(source, target, transformation)
    print(np.mean(t))

def result():
    t = []
    for i in range(0, 10):
        source, target = read_clouds(source_path, target_path)
        neighbor_distance = np.asarray(source.compute_nearest_neighbor_distance())
        coeff = 0.6-(1/neighbor_distance.sum()*100)
        start_time = time()

        source_ransac, target_ransac = read_cloud_voxel_sample_different_cloud(
            0.06, source_path, target_path)
        
        result = execute_global_registration_with_target_density(
            source_ransac, target_ransac)
        source.transform(result.transformation)

        _, target_icp = read_clouds_target_sample(coeff, target_path)
        transformation = registration.ICP_registration(source, target_icp, threshold, -trans_init)
        end_time = time()
        t.append(end_time-start_time)
        #draw_registration_result(source, target, result.transformation)
    print(np.mean(t))
