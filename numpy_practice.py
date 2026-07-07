import numpy as np
arr = np.array([1,2,3,4,5])
print(arr)
print(type(arr))

arr = np.array([10,20,30,40,50])
print(arr+5)
print(arr * 2)
print(arr.sum())
print(arr.mean())
print(arr.max())
print(arr.min())

arr2d = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr2d)
print(arr2d.shape)

print(arr2d[0][0])
print(arr2d[1][1])
print(arr2d[2][2])
