import numpy as np

A =np.array([[1,2],[3,4],[5,6]])
print(A)
print()

#Value extraction
print("a(1,2)=", A[0,1])
print()

#Value modification
A[1,1]=10
print(A)
print()

#Value modification Meyjod 2
A[0,1]= A[0,1]+1
print(A)
print()

##Slicing
print(A[:,0])
print(type(A[:0]))

