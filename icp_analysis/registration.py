import open3d as o3d


def evalution(source, target, threshold, trans_init):
    evaluation = o3d.pipelines.registration.evaluate_registration(
        source, target, threshold, trans_init)
    return evaluation.fitness
    
    
def ICP_registration(source, target, threshold, trans_init, max_iteration=30):
    reg_p2p = o3d.pipelines.registration.registration_icp(
    source, target, threshold, trans_init,
    o3d.pipelines.registration.TransformationEstimationPointToPoint(),
    o3d.pipelines.registration.ICPConvergenceCriteria(max_iteration=max_iteration))
    return reg_p2p.transformation
    