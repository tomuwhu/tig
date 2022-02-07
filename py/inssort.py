from random import shuffle as kever
def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j] :
                arr[j + 1] = arr[j]
                j -= 1
        arr[j + 1] = key
arr = list(range(30))
kever(arr)
print(* arr)
insertionSort(arr)
print(* arr)