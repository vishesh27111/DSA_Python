class SelectionSort:
    def __init__(self, array):
        self.array = array

    def sort(self):
        n = len(self.array)

        for i in range(n-1):
            min = i
            for j in range(i+1, n):
                if self.array[j] < self.array[min]:
                    min = j

            self.array[i], self.array[min] = self.array[min], self.array[i]

        return self.array