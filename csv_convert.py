import numpy as np

file = 'convert_npy/csl_drift_convert.npy'
data = np.load(file)

file_rename = file.replace('.npy','.csv').replace('convert_npy/','convert_npy_csv/')
np.savetxt(file_rename,data,delimiter=',',fmt='%d')