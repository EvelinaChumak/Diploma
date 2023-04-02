import math
import numpy as np
import random as rd


def random_transform(low=-0.02, high=0.02, rotation = 0.02):
    x = rd.uniform(-rotation, rotation)*math.pi/180
    y = rd.uniform(-rotation, rotation)*math.pi/180
    z = rd.uniform(-rotation, rotation)*math.pi/180
    
    cx, cy, cz = math.cos(x), math.cos(y), math.cos(z)
    sx, sy, sz = math.sin(x), math.sin(y), math.sin(z)
    
    return np.asarray([[cz*cy, -sy*sx*cz - sz*cx, -sy*cx*cz + sz*sx, rd.uniform(low,high)],
                       [sz*cy, -sy*sx*sz + cx*cz, -sy*cx*sz - sx*cz, rd.uniform(low,high)],
                       [   sy,             cy*sx,             cy*cx, rd.uniform(low,high)],
                       [  0.0,               0.0,               0.0,                 1.0]]) 
    