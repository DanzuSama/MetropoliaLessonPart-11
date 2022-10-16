print('Supermarket\n ===========')
price_list = [10,14,22,33,44,13,22,55,66,77]
total = 0

def return_price(input):
    input -= 1
    return input


while True:

    user_input = int(input('Please select product (1-10) 0 to Quit: '))
    if user_input == 0:
        print(f'Total: {total}')
        user_input_payment = int(input('Payment: '))
        print('Change:' + str(user_input_payment - total))
        break
    correct_price = return_price(user_input)
    total += price_list[correct_price]
    print(f'Product: {user_input} Price: {price_list[correct_price]}')