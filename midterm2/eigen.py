import numpy as np

arr = np.array([[13.96, 83.465],[83.465,606.94]])

w, v = np.linalg.eig(arr)

print np.max(w)
print "\n"
a = v[np.argmax(w)]
print a


d1 = np.array([61,40])
d2 = np.array([62,120])
d3 = np.array([62,130])
d4 = np.array([68,110])
d5 = np.array([68,141])
d6 = np.array([70,120])
d7 = np.array([70,142])
d8 = np.array([74,180])

print np.dot(a,d1)
print np.dot(a,d2)
print np.dot(a,d3)
print np.dot(a,d4)
print np.dot(a,d5)
print np.dot(a,d6)
print np.dot(a,d7)
print np.dot(a,d8)
