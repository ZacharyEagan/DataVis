import numpy as np

a = np.arange(15).reshape(3,5)
#arrange returns an ndarray from [start,stop) 
#in this case from 0-15) since no start was specified. 
#reshape reorganises the data into a 3X5 ndarray 

print a #just prints out the ndarray


print a.shape  #with no args returns current array dimensions.
#add args to reshape the array but cant change total num of elemints

print a.ndim #takes no args returns num of dimensions of array

print a.dtype.name #takes no args, returns data type of eliments

print a.itemsize #takes no args returns length in bytes of eliments

print a.size #takes no args, returns number of eliments in ndarray

print type(a) #returns type of input

b = np.array([6, 7, 8]) #generates default numpy type array with input
print b #prints b (big suprise)
print type(b) #shows that default numpy array type is an ndarray
