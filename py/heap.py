from random import shuffle as kever
def max_heapify(A,k):
    l = left(k)
    r = right(k)
    if l < len(A) and A[l] > A[k]:
        largest = l
    else:
        largest = k
    if r < len(A) and A[r] > A[largest]:
        largest = r
    if largest != k:
        A[k], A[largest] = A[largest], A[k]
        max_heapify(A, largest)

def left(k):
    return 2 * k + 1

def right(k):
    return 2 * k + 2

def build_max_heap(A):
    n = int((len(A)//2)-1)
    for k in range(n, -1, -1):
        max_heapify(A,k)
arr = list(range(30))
kever(arr)
print(* arr)
build_max_heap(arr)
print(* arr)

# https://favtutor.com/blogs/heap-in-python
