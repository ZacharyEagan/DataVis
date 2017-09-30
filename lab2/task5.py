import numpy as np

a = np.floor(10*np.random.random((3,4)))
print (a)
print (a.shape) #returns shape of the array

print(a.ravel()) #returns a flatened array
a.reshape(6,2) #reshapes array we coverd allready

print("\n\n")
print(a.T) # transpose
print(a.T.shape)
print(a.shape) #note noe of these changed the origional array

print("\n\nresize actually changes the array")
print(a) 
a.resize((2,6))
print(a)

print("\n\n with -1?")
print(a)
a.reshape(3,-1) #-1 here means calculate all other dimensions
print(a)
