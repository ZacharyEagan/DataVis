import numpy as np

#testing out the array printing schema
a = np.arange(6) #first a one dimensional
print (a)
print ("\n\n\n")


b = np.arange(12).reshape(4,3) #now 2d
print (b)
print ("\n\n\n")


c = np.arange(24).reshape(2,3,4) #now a 3d
print(c)
print("\n\n\n")


#now a huge array demonstrating that numpy will obscure 
#uselessly large chunks of daa and just display the edges
d = np.arange(10000)
print(d)
print("\n\n\n")
print(d.reshape(100,100))

#to disable the obscuring use
np.set_printoptions(threshold = 'nan')
#print(d.reshape(100,100)) #but dont cause it's nice the way it was
