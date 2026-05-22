# take any amzoen product and accept the  produt origianl price and discount percentage 
# and calculate the discoutn price and sellign price and pritn on terminal

product_name = input('Enter the product name :')
original_price = float(input('enter the original Price :'))
discount_percentage = float(input('Enter the discount percentage :'))

discount = (discount_percentage / 100) * original_price
selling_price = original_price - discount

print(f'The discout Percentage is {discount}')
print(f'Sellign Pirce is {selling_price}')


