class InsertionSort:
    def __init__(self, array):
        self.array = array

    def sort(self):
        n = len(self.array)
        for i in range(1, n):
            for j in range(i, 0, -1):
                if self.array[j] < self.array[j - 1]:
                    self.array[j], self.array[j - 1] = self.array[j - 1], self.array[j]
                else:
                    break

        return self.array

