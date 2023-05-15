#GeeksforGeeks - Subarray with given sum


class SubArrayTotal:
    def __init__(self, array, total):
        self.array = array
        self.total = total

    def total_indices(self):
        for y in range(len(self.array)):
            for x in range(len(self.array)):
                if x + 1 == len(self.array):
                    if sum(self.array[y:]) == self.total:
                        return [y + 1, self.array.index(self.array[-1]) + 1]
                elif sum(self.array[y:x + 1]) == self.total:
                    return [y + 1, x + 1]
        return "There are no sub-arrays that equal the sum."


test = SubArrayTotal([1, 2, 3, 7, 5], 12)
print(test.total_indices())
