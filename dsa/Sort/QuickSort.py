def partition(array, low, high):
    p = array[high]
    i = low - 1

    for j in range (low, high):
        if array[j] <= p:
            i += 1
            array[i], array[j] = array[j], array[i]

    array[i + 1], array[high] = array[high], array[i + 1]

    return i + 1


class QuickSort:
    # def __init__(self, array):
    #     self.array = array

    def quicksort(self, array, low=0, high=None):
        n = len(array)

        if high is None:
            high = n - 1

        if low < high:
            pivot = partition(array, low, high)
            self.quicksort(array, low, pivot - 1)
            self.quicksort(array, pivot +1, high)

