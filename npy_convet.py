import numpy as np
import matplotlib.pyplot as plt

file = 'extraction_npy/hole_layer.npy'

#origin_data = np.load(file)
#origin_data = np.loadtxt('test.csv',dtype=int,delimiter=',')
convert_data = np.zeros((origin_data.shape[0],origin_data.shape[1]))

for i in range(origin_data.shape[0]):
    for j in range(origin_data.shape[1]):
        if origin_data[i,j] == 0:
            convert_data[i,j] = 0
        else:
            convert_data[i,j] = 100*(38 + (193 - origin_data[i,j]))/38

val_max = 0
val_min = 1000
for i in range(origin_data.shape[0]):
    for j in range(origin_data.shape[1]):
        if val_max < origin_data[i,j]:
            val_max = origin_data[i,j]
        if origin_data[i,j] != 0:
            if val_min > origin_data[i,j]:
                val_min = origin_data[i,j]

print('val max',val_max)
print('val min',val_min)

#convert_data = np.loadtxt('test.csv',dtype=int,delimiter=',')
plt.imshow(origin_data)
#plt.imshow(convert_data)
plt.show()

file_rename = 'convert_npy/' + file.replace('.npy','').replace('extraction_npy/','') + '_convert'

#np.save(file_rename,convert_data)
