from numpy import array as na
from numpy.linalg import solve 
A = na([[1,2,3],[3,2,1],[1,0,1]])
b = na([7,4,5])
print(solve(A,b))