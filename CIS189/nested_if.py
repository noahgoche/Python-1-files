"""
* Name         : <coupon_calculations.py>
* Author       : <Noah Goche>
* Created      : <6/10/2026>
* Course       : CIS189
* IDE          : <Visual Studio Code>
* Description  : <>
*
* Academic Honesty: I attest that this is my original work.
* I have not used unauthorized source code, either modified or
* unmodified.       
"""

# The following is the order of calculations: 

# The first is cash-off coupons. You may apply one $5 or $10 cash off coupon per order.
# The second is percent discount coupons for 10%, 15%, or 20% off.
# The third is tax, 6% of the cost after cash-off and percent discount coupons.
# The fourth is shipping cost (applied to pre-tax amount from step 2):
# up to $10 dollars, shipping is $5.95
# $10 and up to $30 dollars, shipping is $7.95
# $30 and up to $50 dollars, shipping is $11.95
# Shipping is free for $50 and over

# Write a Python program that prompts the user for the the amount of the original purchase price, the cash coupon and the percent coupon. Then calculate and return the total order price for the item.

# For instance, you have $5 off and 30% coupons and the item is $15.99, you will first take:

# $15.99 - $5.00 = $10.99.
# 30% off $10.99 to get $7.69
# Calculate tax at 6% (.06 * 7.69 = 0.46)
# Add shipping cost to pre-tax price (which is $7.69 in this example): $5.95 + $7.69 = $13.64.
# Total cost = 13.64 + .46 = 14.10.