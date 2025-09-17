def isArrayLengthCorrespondsToFullBst(length):

    val = length + 1

    while val > 1:
        remainder = val % 2
        if remainder != 0:
            return False
        val = val // 2

    return length > 0

def GenerateBBSTArray(a):

    if not isArrayLengthCorrespondsToFullBst(len(a)):
        return None

    bbstArray = []
    a.sort()
    borders = []
    borders.append((0, len(a)-1))
    idx = 0

    while idx < len(borders):
        currentBorder = borders[idx]
        leftBorder = currentBorder[0]
        rightBorder = currentBorder[1]

        parentIndex = leftBorder + (rightBorder - leftBorder) // 2
        parent  = a[parentIndex]
        bbstArray.append(parent)

        if leftBorder <=  parentIndex - 1:
            borders.append((leftBorder, parentIndex - 1))
        if parentIndex + 1 <= rightBorder :
            borders.append((parentIndex + 1, rightBorder))
        idx +=1

    return bbstArray