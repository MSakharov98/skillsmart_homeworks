def SynchronizingTables(N, ids, salary):
    sorted_ids = sorted(ids)
    sorted_salary = sorted(salary)

    id_salary_map = {id: salary for id, salary in zip(sorted_ids, sorted_salary)}
    synchronized_salary = [id_salary_map[id] for id in ids]

    return synchronized_salary


