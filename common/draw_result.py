import open3d as o3d
import copy
import matplotlib.pyplot as plt


def draw_registration_result(source, target, transformation):
    source_temp = copy.deepcopy(source)
    target_temp = copy.deepcopy(target)
    source_temp.paint_uniform_color([1, 0.706, 0])
    target_temp.paint_uniform_color([0, 0.651, 0.929])
    source_temp.transform(transformation)
    o3d.visualization.draw_geometries([source_temp, target_temp],
                                      zoom=0.4459,
                                      front=[0.9288, -0.2951, -0.2242],
                                      lookat=[1.6784, 2.0612, 1.4451],
                                      up=[-0.3402, -0.9189, -0.1996])


def show_down_sample_correspondence(down_sample, correspondence):
    plt.plot(down_sample, correspondence)
    plt.xlabel('Down sample')
    plt.ylabel('Correspondence')
    plt.grid(True)
    plt.show()


def show_down_sample_time(down_sample, time):
    plt.plot(down_sample, time)
    plt.xlabel('Down sample')
    plt.ylabel('Time')
    plt.grid(True)
    plt.show()
