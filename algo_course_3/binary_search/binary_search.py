class BinarySearch:
    def __init__(self, sorted_numbers: list[int]):
        self.Numbers = sorted_numbers
        self.Left = 0
        self.Right = len(sorted_numbers) - 1
        self.Status = 0

    def Step(self, number: int):
        if self.Status != 0:
            return

        middle_i = (self.Left + self.Right) // 2
        if middle_i > len(self.Numbers) - 1 or middle_i < 0:
            self.Status = -1
            return

        if self.Numbers[middle_i] == number:
            self.Status = 1
            return

        if self.Numbers[middle_i] < number:
            self.Left = middle_i + 1

        if self.Numbers[middle_i] > number:
            self.Right = middle_i - 1

        if self.Left == self.Right:
            if self.Numbers[self.Left] == number:
                self.Status = 1
            if self.Numbers[self.Left] != number:
                self.Status = -1
            return

        if abs(self.Right - self.Left) == 1:
            if self.Numbers[self.Left] == number or self.Numbers[self.Right] == number:
                self.Status = 1
                return
            self.Status = -1
            return

        if self.Left < 0 or self.Right < 0:
            self.Status = -1
            return

    def GetResult(self) -> int:
        return self.Status