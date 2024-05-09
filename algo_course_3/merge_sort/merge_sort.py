def MergeSort(Array):
    if len(Array) <= 1:
        return Array
    arr1 = MergeSort(Array[0:len(Array)//2])
    arr2 = MergeSort(Array[len(Array)//2:])
    return Merge(arr1, arr2)

# Merge() with removing a first element of subarrays
def Merge(arr1, arr2):
    res = []
    while len(arr1) and len(arr2):
        if arr1[0] <= arr2[0]:
            res.append(arr1[0])
            arr1.remove(arr1[0])
        else:
            res.append(arr2[0])
            arr2.remove(arr2[0])
    while len(arr1):
        res.append(arr1[0])
        arr1.remove(arr1[0])
    while len(arr2):
        res.append(arr2[0])
        arr2.remove(arr2[0])
    return res

# Merge() with i and j -- variable counters
'''
def Merge(arr1, arr2):
    res = []
    i = 0
    j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            res.append(arr1[i])
            i += 1
        else:
            res.append(arr2[j])
            j += 1
    while i < len(arr1):
        res.append(arr1[i])
        i += 1
    while j < len(arr2):
        res.append(arr2[j])
        j += 1
    return res
'''