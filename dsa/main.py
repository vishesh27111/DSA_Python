from dsa.Sort.HeapSort import HeapSort

if __name__ == '__main__':
    arr= [4,3,8,1,2,6,5]
    print(arr)
    sort = HeapSort()
    sort.heapSort(arr)
    print(arr)

