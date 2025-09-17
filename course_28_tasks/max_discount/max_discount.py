def MaximumDiscount(N, price):

    price.sort(reverse=True)

    total_discount = 0

    for i in range(2, N, 3):
        total_discount += price[i]

    return total_discount
