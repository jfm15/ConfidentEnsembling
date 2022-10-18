import numpy as np
import matplotlib.pyplot as plt



ceph_results = np.array([
    [1.562, 1.424, 1.420],
    [1.413, 1.413, 1.406],
    [1.395, 1.392, 1.381],
    [1.493, 1.398, 1.404],
    [1.414, 1.571, 1.419],
    [1.522, 1.476, 1.440],
    [1.524, 1.456, 1.465],
    [1.496, 1.513, 1.472]
])

hand_results = np.array([
    [0.662, 0.648, 0.671],
    [0.636, 0.656, 0.642],
    [0.646, 0.651, 0.647],
    [0.659, 0.657, 0.655],
    [0.671, 0.690, 0.670]
])

pelvis_results = np.array([
    [2.216, 2.281, 2.312],
    [2.633, 2.291, 2.410],
    [2.184, 2.321, 2.296],
    [2.408, 2.268, 2.199],
    [2.294, 2.305, 2.271],
    [2.294, 2.354, 2.238],
    [2.426, 2.420, 2.339],
    [2.385, 2.413, 2.413]
])

ultra_results = np.array([
    [7.776, 7.193, 7.343],
    [7.914, 6.798, 7.113],
    [7.493, 6.856, 7.170],
    [7.080, 7.568, 7.256],
    [6.904, 7.032, 8.962],
    [6.689, 7.031, 6.595],
    [6.986, 7.685, 6.867],
    [7.252, 7.188, 7.131]
])

def print_state(results):
    print("start")
    means = np.mean(results, axis=1)
    stds = np.std(results, axis=1)
    for mean, std in zip(means, stds):
        msg = "{:.3f}$\pm${:.3f}".format(mean, std)
        print(msg)

for arr in [ceph_results, hand_results, pelvis_results, ultra_results]:
    print_state(arr)