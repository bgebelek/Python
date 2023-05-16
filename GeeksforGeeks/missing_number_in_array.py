#GeeksforGeeks - Missing number in array


class ArrayMissingNumber:
    def __init__(self, array):
        self.array = array

    def find_missing_number(self):
        sorted_array = sorted(self.array)
        index_a, index_b = 0, 1
        for _ in range(len(sorted_array)):
            if sorted_array[index_b] - sorted_array[index_a] != 1:
                return sorted_array[index_a] + 1
            index_b += 1
            index_a += 1


test = ArrayMissingNumber([1, 2, 5, 6, 3])
print(test.find_missing_number())
