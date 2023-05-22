#GeeksforGeeks - Sum of Series


class SumOfSeries:
    def __init__(self, number):
        self.number = number

    def return_sum_of_series(self):
        if self.number < 0:
            return "The number must be positive."
        elif self.number == 0:
            return 0
        return sum(range(self.number + 1))


test = SumOfSeries(int(input("Number: ")))
print(test.return_sum_of_series())
