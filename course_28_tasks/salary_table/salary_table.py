def SynchronizingTables(N, ids, salary):

    sorted_salary = salary.copy()

    sorted_salary.sort()

    mapping = dict(zip(ids, sorted_salary))

    synchronized_salary = [mapping[id] for id in ids]

    return synchronized_salary
