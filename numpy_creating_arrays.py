import numpy as np

# arr = np.array([1, 2, 3, 4, 5])

# print(arr)

# print(type(arr))


# # use list to create ndarray
# arr = np.array([1, 2, 3, 4, 5])

# # use tuple to create ndarray
# arr = np.array((1, 2, 3, 4, 5))


# # dimentions in arrays

# # 0-D
# arr = np.array(42)
# print(arr)

# # 1-D
# arr = np.array([1, 2, 3, 4, 5])
# print(arr)

# # 2-D
# arr = np.array([[1, 2, 3], [4, 5, 6]])
# print(arr)

# # 3-D
# arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
# print(arr)


# a = np.array(42)
# b = np.array([1, 2, 3, 4, 5])
# c = np.array([[1, 2, 3], [4, 5, 6]])
# d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

# print(a.ndim)
# print(b.ndim)
# print(c.ndim)
# print(d.ndim)


arr = np.array([1, 2, 3, 4], ndmin=5)

print(arr)
print("number of dimetnsions: ", arr.ndim)