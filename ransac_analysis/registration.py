from common.cloud_information import cloud_density
import open3d as o3d
import copy


def preprocess_point_cloud(cloud):
    cloud_tmp = copy.deepcopy(cloud)
    density = cloud_density(cloud_tmp)
    radius_normal = density * 2
    cloud_tmp.estimate_normals(
        o3d.geometry.KDTreeSearchParamHybrid(radius=radius_normal, max_nn=30))

    radius_feature = density * 2
    pcd_fpfh = o3d.pipelines.registration.compute_fpfh_feature(
        cloud_tmp,
        o3d.geometry.KDTreeSearchParamHybrid(radius=radius_feature, max_nn=100))
    return cloud_tmp, pcd_fpfh


def execute_global_registration_with_target_density(source_cloud, target_cloud):
    print(cloud_density(source_cloud)/cloud_density(target_cloud))
    distance_threshold = cloud_density(target_cloud) * 1.5
    source, source_fpfh = preprocess_point_cloud(source_cloud)
    target, target_fpfh = preprocess_point_cloud(target_cloud)
    result = o3d.pipelines.registration.registration_ransac_based_on_feature_matching(
        source = source, 
        target = target, 
        source_feature = source_fpfh, 
        target_feature = target_fpfh, 
        mutual_filter = True,
        max_correspondence_distance = distance_threshold,
        estimation_method = o3d.pipelines.registration.TransformationEstimationPointToPoint(False),
        ransac_n = 3, 
        checkers = [
            o3d.pipelines.registration.CorrespondenceCheckerBasedOnEdgeLength(
                0.9),
            o3d.pipelines.registration.CorrespondenceCheckerBasedOnDistance(
                distance_threshold)
        ], 
        criteria = o3d.pipelines.registration.RANSACConvergenceCriteria(100000, 0.999))
    return result
