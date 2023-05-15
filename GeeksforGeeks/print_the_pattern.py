#GeeksforGeeks - Print the pattern


class PrintPattern:
    def __init__(self, number):
        self.number = number

    def print_pattern(self):
        if 1 <= self.number <= 40:
            result = ""
            for x in range(1, self.number + 1):
                result += "$"
                for y in range(self.number, 0, -1):
                    result += str(y) * x
            return result
        else:
            return "Number must be between 1 and 40 (both are inclusive)."


test = PrintPattern(int(input("Number: ")))
print(test.print_pattern())
