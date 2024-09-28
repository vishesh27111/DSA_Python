class BubbleSort:
    def __init__(self, array):
        self.array = array
        self.size = len(array)

    def sort(self):

        for i in range(self.size - 1):
            swapped = False
            for j in range(self.size - i - 1):
                if self.array[j] > self.array[j + 1]:
                    self.array[j], self.array[j + 1] = self.array[j + 1], self.array[j]
                    swapped = True
            if not swapped:
                break

        return self.array