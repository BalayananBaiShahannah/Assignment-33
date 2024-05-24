import numpy as np

# Example 1
loaded_arr1_from_np = np.load('array.npy')

# Example 2
loaded_data_custom = np.genfromtxt('data_custom.csv', delimiter=',')

# Example 3
npzfile_structured = np.load('structured_data.npz')
loaded_arr_structured = npzfile_structured['arr_structured']
