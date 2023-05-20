import open3d as o3d
from common.cloud_information import cloud_density


def read_clouds_target_sample(down_sample, data):
    demo_icp_pcds = data
    source = o3d.io.read_point_cloud(demo_icp_pcds)
    target = o3d.io.read_point_cloud(demo_icp_pcds).random_down_sample(down_sample)
    return source, target


def read_clouds_source_sample(down_sample, data):
    demo_icp_pcds = data
    source = o3d.io.read_point_cloud(demo_icp_pcds).random_down_sample(down_sample)
    target = o3d.io.read_point_cloud(demo_icp_pcds)
    return source, target

def read_clouds_voxel_sample(down_sample, data):
    demo_icp_pcds = data
    source = o3d.io.read_point_cloud(demo_icp_pcds).random_down_sample(0.6)
    target = o3d.io.read_point_cloud(demo_icp_pcds).random_down_sample(0.6)
    voxel_sample = (cloud_density(source)+cloud_density(target))/(2*down_sample)
    source = source.voxel_down_sample(voxel_sample)
    target = target.voxel_down_sample(voxel_sample)
    return source, target

def read_clouds_voxel_sample_withot_down_sample(down_sample, data):
    demo_icp_pcds = data
    source = o3d.io.read_point_cloud(demo_icp_pcds)
    target = o3d.io.read_point_cloud(demo_icp_pcds)
    voxel_sample = (cloud_density(source)+cloud_density(target))/(2*down_sample)
    source = source.voxel_down_sample(voxel_sample)
    target = target.voxel_down_sample(voxel_sample)
    return source, target

def read_clouds_voxel_sample_from_documentation(data1, data2):
    source = o3d.io.read_point_cloud(data1).voxel_down_sample(0.05)
    target = o3d.io.read_point_cloud(data2).voxel_down_sample(0.05)
    return source, target

def read_clouds(data1, data2):
    source = o3d.io.read_point_cloud(data1)
    target = o3d.io.read_point_cloud(data2)
    return source, target

def read_cloud_voxel_sample_different_cloud(down_sample, data1, data2):
    source = o3d.io.read_point_cloud(data1)
    target = o3d.io.read_point_cloud(data2)
    voxel_sample = (cloud_density(source)+cloud_density(target))/(2*down_sample)
    source = source.voxel_down_sample(voxel_sample)
    target = target.voxel_down_sample(voxel_sample)
    return source, target
