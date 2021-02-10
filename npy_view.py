import numpy as np
import matplotlib.pyplot as plt

file = 'convert_npy\gate_convert.npy'
data = np.load(file)

plt.imshow(data)
plt.show()