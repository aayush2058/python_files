products = [{'name':'pixel 7', 'type':'phone', 'price':'699'},
            {'name':'nitro 5', 'type':'laptop', 'price':'1499'},
            {'name':'tune 600', 'type':'headphone', 'price':'99'},
            {'name':'flip 5', 'type':'portable speaker', 'price':'129'}]

# features
# 1. Products must be displayed to the user in proper format
# 2. User should get a cart to add products
# 3. User should be able to add product until they donot want to any further
# 4. Quantity of products must be counted and if same product is added multiple times, quantity value must be increased
# 5. Total amount should be displayed to the user along with cart


cart = []
total = 0
for index, each_product in enumerate(products):
    print(f"{index+1} {each_product['name']}  :  {each_product['type']}  :  ${each_product['price']}")

buy = input(f"Here are some of the products trending today. What would you like to add them to your cart? ")


if buy == 'yes' or buy == 'ofcourse':
    while True:
        want_product = input('Enter the id of the product you would like to buy  :  ')

        wanted_product = (products[int(want_product) - 1])

        if wanted_product in cart:
            wanted_product['quantity'] += 1

        else:
            wanted_product['quantity'] = 1
            cart.append(wanted_product)

        for each_products in cart:
            print(f"{each_products['name']}  :  {each_products['type']}  :  ${each_products['price']}, quantity - {each_products['quantity']}")

        total += int(each_products['price'])


        do_you = input('Do you want to shop more? ')
        if do_you == 'yes':
            continue

        else:
            break
    print(f'Here are all of the items you purchased.')
    print()
    for each_products in cart:
        print(
            f"{each_products['name']}  :  {each_products['type']}  :  ${each_products['price']}, quantity - {each_products['quantity']}")
    print()
    print(f'Thankyou for shopping with us! Your total is ${total}. Have a wonderful week✌️')
    print('Your items will be delivered soon.')

else:
    print('Have a good time !')

