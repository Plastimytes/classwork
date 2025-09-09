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
print()

#Slicing method2
a=A[:,0]
print(a)
print(type(a))
print()

#Extracting rows
print(A[1,:])
print()

#Extracting a 2*2 block from a 3*3 matrix
B = np.array([[1,2,3], [4,5,6], [7,8,9]])


C=B[0:2, 0:2]

print(C)
