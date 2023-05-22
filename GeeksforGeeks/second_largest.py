#GeeksforGeeks - Second Largest


class SecondLargest:
    def __init__(self, numbers, length):
        self.numbers = numbers
        self.length = length

    def find_second_largest(self):
        if self.length >= 2:
            sorted_numbers = sorted(self.numbers)
            for index in reversed(range(self.length)):
                if sorted_numbers[index] < max(self.numbers):
                    return sorted_numbers[index]
            return -1
        else:
            return -1


test = SecondLargest([6, 6, 3, 6, 6], 2)
print(test.find_second_largest())
