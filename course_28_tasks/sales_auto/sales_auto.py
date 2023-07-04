def ShopOLAP(N, items):

    if N < 1:
        raise ValueError

    sales = {}

    for item in items:
        name, quantity = item.split()
        if name in sales:
            sales[name] += int(quantity)
        else:
            sales[name] = int(quantity)

    sorted_sales = sorted(sales.items(), key=lambda x: (-x[1], x[0]))

    result = []
    for item in sorted_sales:
        result.append(item[0] + ' ' + str(item[1]))

    return result
