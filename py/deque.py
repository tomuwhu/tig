from collections import deque
d = deque([1,2,3,4,5,6])
for elem in d:
     print(elem ** 2)
d.append(7)
print("----")
print( d.popleft() )
print( d.popleft() )
print( list(d) )
d.rotate(3)
print( list(d) )