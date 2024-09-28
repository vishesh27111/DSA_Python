from pstats import SortKey

from dsa.Sort.BubbleSort import BubbleSort
from dsa.Sort.InsertionSort import InsertionSort
from dsa.Sort.SelectionSort import SelectionSort

if __name__ == '__main__':
    arr= [4,3,8,1,2,6,5]
    print(arr)
    sort = InsertionSort(arr)
    sorted_arr = sort.sort()

    print(sorted_arr)