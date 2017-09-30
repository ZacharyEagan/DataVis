import numpy as np
from numpy import pi
#arithmetic on arrays is performed on all eliments
#forms new array, so careful about efficiency please

a = np.array([20,30,40,50])
print (a)
b = np.arange(4)
print (b)
print("\n\na-b")
c = a - b
print (c)
print("\n\nb ** 2")
print (b ** 2)
print("\n\n10 * sin(a)")
print (10 * np.sin(a))
print("\n\na < 35")
print (a < 35)



#dot product has a method not an opperator

a = np.array([[1,1],[0,1]])
b = np.array([[2,0],[3,4]])
print("\n\n a * b")
print(a*b) #multiplication is elimentwise

print("\n\n a.dot(b) && np.dot(a,b)")

print(a.dot(b)) #dot product requires method
print("\n\n")
print(np.dot(a,b))

#with = means no new array
a = np.ones((2,3), dtype=int)
b = np.random.random((2,3))

print("\n\n a*=3")
a*=3
print (a)

print("\n\nb += a")
b+=a
print(b)

print("\n\n a += b")
#a += b #does not work do to inability to downcast?
print (a)

print("\n\n")

print("\n\n upcasting demo\n")
#data is always upcasted to whichever datatype will best fit

a = np.ones(3, dtype=np.int32)
b = np.linspace(0,pi,3)
print("b type")
print(b.dtype.name)
print("a type")
print(a.dtype.name)

c = a+b
print ("c = a + b")
print (c)
print (c.dtype.name)
d = np.exp(c*1j)
print ("d = c * 1j")
print (d)
print (d.dtype.name)

print("\n\n\n\n unary examples")
#UNARY operations implimented as methods of ndarray
a = np.random.random((2,3))
print("a")
print (a)
print("a.sum")
print (a.sum())
print("a.min")
print (a.min())
print("a.max")
print (a.max())

#can do the unary's but apply just to one axis
b = np.arange(12).reshape(3,4)
print (b)
print (b.sum(axis=0))
print (b.min(axis=1))
print (b.cumsum(axis=1))
