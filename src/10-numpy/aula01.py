import numpy as np
import numpy.random as rng

a = np.array([1,2,3,4,5,6],[3,2,1,2,5])
print(a)
print(type(a))

zero_array = np.zeros(shape = (5,3,6))
print(zero_array)

um_array = np.ones(shape = (2,3))
print(um_array)

arr = np.arange(10,200,30)
print(arr)
array_linear = np.linspace(0,100,num = 20,endpoint = False)
print(array_linear)

print(zero_array.size)
print(zero_array.shape)

a = np.array([1,2,3])
a21 = a[:,np.newaxis]
b = np.array([1,2,34,5,6])
c = np.concatenate(a,b)
maior = a[a/2 == 0]
print(a)
print(b)
print(c)
print(maior)
print(a.min())
print(a.max())

aleatorio = rng.integers(20, size = (2,4))
print(aleatorio)