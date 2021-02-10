import numpy as np
import matplotlib.pyplot as plt

file = 'convert_npy/csl_drift_convert.npy'
data = np.load(file)
hole_layer = np.zeros(data.shape,dtype=int)
#121 111

for i in range(123,data.shape[0]):
    for j in range(data.shape[1]):
        if data[i,j] == 0:
            for next_to in range(20):
                try:
                    if data[i+next_to,j] != 0 or data[i,j+next_to] != 0:
                        hole_layer[i,j] = 100
                except:
                    pass

                try:
                    if data[i-next_to,j] != 0 or data[i,j-next_to] != 0:
                        hole_layer[i,j] = 100
                except:
                    pass

plt.imshow(hole_layer)
plt.show()