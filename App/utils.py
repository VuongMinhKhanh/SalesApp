def count_cart(cart):
    total_amount, total_quantity = 0, 0

    if cart:
        for c in cart.values():
            total_quantity += c["quantity"]
            # print(c["price"])
            total_amount += c["quantity"] * c["price"]
    return {
        "total_amount": total_amount,
        "total_quantity": total_quantity
    }