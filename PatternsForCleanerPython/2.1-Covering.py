# Python’s assert statement is a debugging aid, not a mechanism for handling run-time errors.

def apply_discount(product, discount):
    price = int(product['price'] * (1.0 - discount))
    assert 0 <= price <= product['price']
    return price


shoes = {'name': 'Fancy Shoes', 'price': 14900}

if __name__ == '__main__':
    print(apply_discount(shoes, 0.25))
    print(apply_discount(shoes, 2))  # AssertionError

# if __debug__:
#     if not expression1:
#         raise AssertionError(expression2)


# 1. Don’t Use Asserts for Data Validation
# Wrong Sample
"""
def delete_product(prod_id, user):
    assert user.is_admin(), 'Must be admin'
    assert store.has_product(prod_id), 'Unknown product'
    store.get_product(prod_id).delete()
"""
# Correct Sample
"""
def delete_product(product_id, user):
    if not user.is_admin():
        raise AuthError('Must be admin to delete')
    if not store.has_product(product_id):
        raise ValueError('Unknown product id')
    store.get_product(product_id).delete()
"""

# 2. Asserts That Never Fail
# assert(1 == 2, 'This should fail') #
"""
If you pass a tuple to an assert statement, it leads to the assert condition
always being true—which in turn leads to the above assert statement
being useless because it can never fail and trigger an exception.
"""