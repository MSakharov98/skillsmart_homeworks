'''
Так как у студента отсутствует доступ к первому курсу,
где был написан код алгоритма сортировки,
реализуем сортировку пузырьком
'''

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
