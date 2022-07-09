import numpy as np
import sys
import time

## Loop through using numpy
li_ar = [i for i in range(0, 100)]
np_ar = np.arange(100)

print(li_ar)
print(np_ar)

## Size of one element in numpy array [in bytes]
print(np_ar.itemsize)
## Size of 100 elements in numpy array [in bytes]
print(np_ar.itemsize * np_ar.size)

## Size of one element in list
print(sys.getsizeof(10))
## Size of 100 elements in list
print(sys.getsizeof(1) * len(li_ar))

size = 100000


## Time comparison for adding of array a and b
def add_using_list():
    t1 = time.time()
    a = range(size)
    b = range(size)
    c = [a[i] + b[i] for i in range(size)]
    t2 = time.time()
    return t2 - t1


def add_using_numpy():
    t1 = time.time()
    a = np.arange(size)
    b = np.arange(size)
    c = a + b
    t2 = time.time()
    return t2 - t1


t_list = add_using_list()
t_numpy = add_using_numpy()
print("List:", t_list * 1000, "ms")
print("Numpy:", t_numpy * 1000, "ms")

"""
So above explanations gives us the idea that how numpy is faster, memory saving
functionality and convenience for a programmer
"""

# Array creation in numpy
a = [1, 2, 3]
b = np.array(a)
print(b)

# Array in Numpy have a homogeneous data-type
a = [1, 2, 3, '5', 4]
b = np.array(a)
print(b)

# We can convert the data type of the array
a = [1, 2, 3, '5', 4]
b = np.array(a, dtype=int)
print(b)

# Filling array with one specific element inBuilt
b = np.ones(3, dtype=int)
print(b)

# Filling array with one specific element
b = np.full(3, 5, dtype=int)
print(b)

# Filling 2d-array with one specific element
b = np.ones((2, 3), dtype=int)
print(b)

# Arange function:
b = np.arange(2, 10)
print(b)
b = np.arange(2, 10, 2)
print(b)

# linspace function:
b = np.linspace(2, 10)
print(b)
print(b[1] - b[0])

# identity function:
print(np.identity(3))

# eye function:
print(np.eye(3, 4))

# random function
print(np.random.random(3))

# Few other function
print(np_ar.data)
print(np_ar.shape)
print(np_ar.dtype)
print(np_ar.strides)

# On 2d array
np_ar_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(np_ar_2d.data)
print(np_ar_2d.shape)
print(np_ar_2d.dtype)
print(np_ar_2d.strides)

# Mathematical Operation on Numpy array
a = np.random.randint(1, 20, 5)
b = np.random.randint(1, 20, 5)
a = a + 1
print(a)

# Mathematical Functions
print(a.sum())
print(a.mean())
print(a.min())
print(a.argmin())
print(a.max())
print(a.argmax())

#Logical Operations
print(np.logical_or(a, b))
print(np.logical_and(a, b))
print(np.logical_not(a))
print(np.logical_xor(a, b))

#Braodcasting

'''
Broadcasting is the concept of dimension mismatch comparing
Numpy can compare -->
1. Array with equal size
2. One of them size is 1

e.g.    Array1                Array2
         3,2                   3,2       ---> correct
         3,3                   3,2       ---> wrong
         3,3                   3,1       ---> correct
'''

x = np.random.randint(1, 10, (3, 3))
y = np.random.randint(1, 10, 3)
print(x - y)

# Transpose function
y = np.transpose(y)
print(y)