import numpy as np

arr01 = np.array([[0, 1, 2], [3, 4, 5]],
               dtype=np.float32)
''' NumPy arrays are basically just Python 
lists with added features. In fact, you can
easily convert a Python list to a Numpy array
using the np.array function, which takes in
a Python list as its required argument. 
The function also has quite a few keyword 
arguments, but the main one to know is dtype. 
The dtype keyword argument takes in a NumPy 
type and manually casts the array to the specified type.'''
               
print("1st print -", repr(arr01))


''' The code below is an example of np.array upcasting. 
Both integers are cast to their floating-point equivalents.'''
arr02 = np.array([0, 0.1, 2])
print("2nd print - ", repr(arr02))
print("type of this - ", type(arr02[0]))

'''Same goes for the below just the type will be string'''
arr03 = np.array([0, 0.1, "2"])
print("2nd print - ", repr(arr03))
print("type of this - ", type(arr03[0]))


##COPYING

''' In the code example below, c is a reference to a while 
d is a copy. Therefore, changing c leads to the same change 
in a, while changing d does not change the value of b. '''

a = np.array([0, 1])
b = np.array([9, 8])
c = a
print('Array a: {}'.format(repr(a)))
c[0] = 5
print('Array a: {}'.format(repr(a)))

d = b.copy()
d[0] = 6
print('Array b: {}'.format(repr(b)))


#CASTING

'''The code below shows an example of casting using 
the astype function. The dtype property returns the type of an array.'''

arr04 = np.array([0, 1, 2])
print("Before casting - ",arr04.dtype)
arr05 = arr04.astype(np.float32)
print("After casting - ",arr05.dtype)


#NaN

'''When we don't want a NumPy array to contain a value at a particular 
index, we can use np.nan to act as a placeholder. A common usage for 
np.nan is as a filler value for incomplete data.'''
'''The code below shows an example usage of np.nan. 
Note that np.nan cannot take on an integer type.'''

arr = np.array([np.nan, 1, 2])
print("NaN represenattion - ",repr(arr))

arr = np.array(["NaN represenattion for string - ",np.nan, 'abc'])
print(repr(arr))

# Will result in a ValueError
#np.array([np.nan, 1, 2], dtype=np.int32)


#INFINITY

'''To represent infinity in NumPy, we use the np.inf special value.
 We can also represent negative infinity with -np.inf.

The code below shows an example usage of np.inf. 
Note that np.inf cannot take on an integer type.'''

print("Checking - ",np.inf > 1000000)

arr = np.array([np.inf, 5])
print(repr(arr))

arr = np.array([-np.inf, 1])
print(repr(arr))

# Will result in an OverflowError
#np.array([np.inf, 3], dtype=np.int32)

#coding - direct

# CODE HERE
arr = np.array([np.nan, 2,3,4,5])

# CODE HERE

arr2 = arr.copy()
arr2[0] = 10

# CODE HERE
float_arr = np.array([1,5.4,3])

float_arr2= arr2.astype(np.float32)

float_arr = np.array([1, 5.4, 3])
float_arr2 = arr2.astype(np.float32)

matrix = np.array([[1,2,3],[4,5,6]], dtype=np.float32)

