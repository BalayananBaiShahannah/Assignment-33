import numpy as np

# Example 1
arr1 = np.array([[54, 14, 10], [7, 12, 19]])
np.save('array.npy', arr1)

# Example 2
dtype = [('name', 'S10'), ('age', int)]
values = [('Bai', 18), ('Shahannah', 20), ('Balayanan', 22)]
arr_structured = np.array(values, dtype=dtype)
np.savez('structured_data.npz', arr_structured=arr_structured)

# Example 3
data = np.random.rand(10, 6)
header = 'Column1,Column2,Column3'
np.savetxt('data.csv', data, delimiter=',', header=header)