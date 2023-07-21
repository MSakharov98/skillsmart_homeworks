def EEC_help(arr1, arr2):

    if len(arr1) != len(arr2):
        return False

    count1 = {}
    count2 = {}

    for num in arr1:
        count1[num] = count1.get(num, 0) + 1

    for num in arr2:
        count2[num] = count2.get(num, 0) + 1

    return count1 == count2
