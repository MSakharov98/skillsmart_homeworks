def massdriver(activate):

    visited = set()
    dup = {x for x in activate if x in visited or (visited.add(x) or False)}

    if list(dup):
        return activate.index(list(dup)[0])

    return -1