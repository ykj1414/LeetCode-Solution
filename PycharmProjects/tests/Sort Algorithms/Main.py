from XuanZe import selectSort
from Insert import insertSort
from QuickSort import quickSort,quick3Sort
from Shell import shellSort
from Merge import mergeSort1,mergeSort2
from HeapSort import heapSort

if __name__ == "__main__":
    # n = int(input())
    # a = [n-i for i in range(n)]
    # a = [1,5,2,7,8,0,10,9,1,1,2,3,4,5,1,10,7,8,6]
    # a = ['R','B','W','W','R','W','B','R','R','W','B','R']
    a = ['S', 'O', 'R', 'T', 'E', 'X', 'A', 'M', 'P', 'L', 'E']
    b = a.copy()
    print(a)
    # selectSort(a)
    # insertSort(a)
    # quick3Sort(a)
    # quickSort(b)
    # print(a)
    # shellSort(a)
    # mergeSort1(a)
    # print(a)
    # mergeSort2(a)
    heapSort(a)
    print(a)
