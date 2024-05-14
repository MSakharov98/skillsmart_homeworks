class BinarySearch:

    def __init__(self, array):
        self.Array = array
        self.Left_index = 0
        self.Right_index = len(array) - 1
        self.Finding_status = 0

    def Step(self, Finding_value):
        if self.Finding_status == 0:
            middle_index = (self.Left_index + self.Right_index) // 2
            if self.Left_index > self.Right_index:
                self.Finding_status = -1
                return
            if Finding_value == self.Array[middle_index]:
                self.Finding_status = 1
            elif Finding_value > self.Array[middle_index]:
                self.Left_index = middle_index + 1
            else:
                self.Right_index = middle_index - 1
            if self.Left_index > self.Right_index:
                self.Finding_status = -1
            elif self.Right_index - self.Left_index <= 1:
                if Finding_value in (self.Array[self.Left_index], self.Array[self.Right_index]):
                    self.Finding_status = 1
                    return
                self.Finding_status = -1

    def GetResult(self):
        return self.Finding_status


def GallopingSearch(array, finding_value, start_index=1):
    current_index = 2 ** start_index - 2
    if current_index < len(array) - 1:
        if array[current_index] == finding_value:
            return True
        if array[current_index] < finding_value:
            return GallopingSearch(array, finding_value, start_index + 1)
    else:
        current_index = len(array) - 1
    searcher = BinarySearch(array)
    searcher.Left_index = 2 ** (start_index - 1) - 1
    searcher.Right_index = current_index
    while searcher.Finding_status == 0:
        searcher.Step(finding_value)
    if searcher.Finding_status == -1:
        return False
    else:
        return True
