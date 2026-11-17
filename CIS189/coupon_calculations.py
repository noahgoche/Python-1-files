"""
* Name         : <coupon_calculations.py>
* Author       : <Noah Goche>
* Created      : <6/10/2026>
* Course       : CIS189
* IDE          : <Visual Studio Code>
* Description  : <Takes an original price, cash coupon, and percent coupon to calculate
                  the price of an item after coupons, taxes, and shipping costs are applied>
*
* Academic Honesty: I attest that this is my original work.
* I have not used unauthorized source code, either modified or
* unmodified.       
"""

price = float(input("Enter the original price of the item: "))
cash_coupon = float(input("Enter the cash coupon value: "))
percent_coupon = float(input("Enter the percent coupon: "))

pre_tax_price = (price - cash_coupon) * (1 - (percent_coupon/100))

post_tax_price = pre_tax_price * (1.06)

if pre_tax_price < 10:
    shipping_cost = 5.95
elif 10 <= pre_tax_price < 30:
    shipping_cost = 7.95
elif 30 <= pre_tax_price < 50:
    shipping_cost = 11.95
else:
    shipping_cost = 0

total_cost = post_tax_price + shipping_cost
total_cost = round(total_cost, 2)

print("The total cost is ", total_cost)