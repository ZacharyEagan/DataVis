import numpy as np

#showing that python will automaticall determin array type based on 
# the eliments stored
a = np.array([2,3,4])
print a
print a.dtype

#for example this one produces an array of float types
b = np.array([1.2, 2.3, 3.3, 3.4])
print b
print b.dtype


#question: what happens in a mixed type array?
c = np.array([1.2,5,6,7])
print c
print c.dtype

d = np.array([6,7,8,1.2])
print d
print d.dtype

#answer: apears it uses whatever datatype will be least lossy overall
#so if a float is present it uses float since that also can hold int

#looks like numpy is fine handling complex numbers so long as specified
e = np.array([[1,2],[3,4]], dtype=complex) #can specify type manually 
print e
print e.dtype #has a native type for complex nums

f = np.array([6,7,8,1.2], dtype=int)#does not warn about loss if type
#is manually specified
print f


g = np.zeros((3,4)) #aray of dimensions filled with zeros
print "\ng"  #starting to get messy so adding lables and line breaks
print g

h = np.ones((2,3,4), dtype=np.int16) #specify datatype fill with zeros
print "\nh"
print h

i = np.empty((2,3)) #random data default datatype is float
print "\ni"
print i


#now testing the arrange function with different datatypes
j = np.arange(10,30,5) #generates numbers from [10-30) in steps of 5
print "\n\nj"
print j

k = np.arange(0,2,0.3) #generates values from 0 to 2 in steps of .3
print "\nk"
print k


print "\n\n\n"

from numpy import pi
l = np.linspace(0,2,9) # for generating floats linspace is better
#generates 9 numbers from [0-2)
print l

m = np.linspace(0, 2*pi, 100) #using the pi constant
print m
print "\n\n"

n = np.sin(m)  #because python is rediculous passing an unknown array
#like m into the sin function will simply evaluate sin over all m
#and return another array of the outputs
print n
#pretty cool
