#%%
import numpy as np
from numpy.random import random
import matplotlib.pyplot as plt
from scipy import misc
from PIL import Image


my_array = np.array([1.1, 9.2, 8.1, 4.7])

print(my_array.shape)
# can call like a list 
print(my_array[2])
print(my_array.ndim)

array_2d = np.array([[1, 2, 3, 9], [5, 6, 7, 8]])

print(f'array_2d has {array_2d.ndim} dimensions')
print(f'Its shape is {array_2d.shape}')
print(f'It has {array_2d.shape[0]} rows and {array_2d.shape[1]} columns')
print(array_2d)
# access the 3rd value in the 2nd row
print(array_2d[1,2])
# access an entire row and all the values
print(array_2d[0, :])

array_3d = np.array([[[0, 1, 2, 3],
                    [4, 5, 6, 7]],

                    [[7, 86, 6, 98],
                    [5, 1, 0, 4]],
                          
                    [[5, 36, 32, 48],
                    [97, 0, 27, 18]]])
print(array_3d.shape)
print("a",array_3d[2, 1, 3])
print("b",array_3d[2,1:])
print(array_3d[0,:,:])
print(array_3d[:,0,:])
print(array_3d[:,:,0])
print(f'We have {array_3d.ndim} dimensions')
print(f'Its shape is {array_3d.shape}')

a = np.arange(10, 30)
b = a[-3:]
c = a[3:6]
d = a[12:]
e = a[::2]
print(e)
# a = a[::-1]
a = np.flip(a)
print(a)

# C4
a = [6,0,9,0,0,5,0]
# print non-zero values
nz_indices = np.nonzero(b)
print(nz_indices)
print([b for b in a if b != 0])

# create 3x3x3 matrix with random values
b = random((3,3,3))
print(b)

x = np.linspace(0, 100, num=9)
print(x)

y = np.linspace(-3, 3, num=9)
print(y)

plt.plot(x,y)

noise = np.random.random((128,128,3))
print(noise.shape)
plt.imshow(noise)

# Numpy functions
v1 = np.array([4, 5, 2, 7])
v2 = np.array([2, 1, 3, 3])
# addition
v1 + v2
# can use scalars also
print(v1 + 10)
print(v1 * 2)


a1 = np.array([[1, 3],
               [0, 1],
               [6, 2],
               [9, 7]])
 
b1 = np.array([[4, 1, 3],
               [5, 8, 5]])


c1 = np.matmul(a1,b1)
print("c1", c1)

img = misc.face()
plt.imshow(img)
print(img)
print(type(img))
print(img.ndim)
print(img.shape)

img = img/255
grey_vals = np.array([0.2126, 0.7152, 0.0722])
grey_img = np.matmul(img, grey_vals)

plt.imshow(grey_img, cmap='gray')

flipped_img = np.flip(grey_img)
plt.imshow(flipped_img, cmap='gray')

rotated_img = np.rot90(img)
plt.imshow(rotated_img)

invert_img = grey_img * -1
invert_img = 255-img
plt.imshow(invert_img)

image = 'C:/Users/RSiu9/OneDrive/Documents/GitHub/RoySiu.github.io/Udemy 100 Days of Code/Day 77/yummy_macarons.jpg'

my_img = Image.open(image)
img_array = np.array(my_img)

print(img_array.ndim)
print(img_array.shape)
plt.imshow(img_array)

plt.imshow(255-img_array)
# %%
