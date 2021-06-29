import numpy as np
# Original matrix
A = np.array([[1,2,3],[3,-2,1],[4,2,1]])
I = np.array([[1,0,0],[0,1,0],[0,0,1]])
print("Original matrix:")
print(A)

W= np.dot(A,A)
x= np.dot(A,W)  
y=23*A
z=40*I
p=x-y-z
result = p
print('Value of A^3 is:')
print(x)
print('Value of 23A is:')
print (y)
print('Value of 40I is:')
print(z)
print('Value of A^3-23A-40I is :')
print(result)
