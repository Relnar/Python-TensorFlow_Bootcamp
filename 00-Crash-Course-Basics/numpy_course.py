import numpy as np

print("")

my_list = [1,2,3]
arr = np.array(my_list)
print(type(arr))
print(np.arange(0, 10, 2))

# 2D array
print(np.zeros((3, 5)))
print(np.ones((3,5)))

# linear space
print(np.linspace(0, 11, 10))

# random
print(np.random.randint(0, 11, (3,3)))
print(np.random.normal())

# random seed
np.random.seed(101)
arr = np.random.randint(0, 100, 10)

print(arr)
print(arr.max(), arr.min(), arr.mean(), arr.argmax())

# reshape
print(arr.reshape(2,5))

mat = np.arange(0, 100).reshape(10, 10)
print(mat)
# [row, col]
print(mat[0,1])
print(mat[:, 0])
print(mat[0:3, 0:3])

# filter
my_filter = mat > 50
print(my_filter)
print(mat[my_filter])

print("")