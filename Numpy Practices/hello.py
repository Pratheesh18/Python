import numpy as np

# arr = np.array([1,2,3,4,5])
# print(arr)

# arr = np.array([[1,2,3],[4,5,6]]) #2D array
# print(arr)

a = np.array(42)
b = np.array([1,2,3,4,5])
c= np.array([[1,2,3] , [4,5,6]])
d = np.array([[[1,2,3] , [4,5,6]] , [[1,2,3] , [4,5,6]]])

print(a.ndim)
print(d.ndim) # it will tell how many dimensions that hold array

arr =np.array([1,2,3,4], ndmin=5)
print(arr)
print('number of dimensions : ', arr.ndim)