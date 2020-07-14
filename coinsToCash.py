def calc_dollars(**coins):
    dollarAmount = 0

    dollarAmount += coins['pennies'] * .01
    dollarAmount += coins['nickels'] * .05
    dollarAmount += coins['dimes'] * .10
    dollarAmount += coins['quarters'] * .25

    print(dollarAmount)


calc_dollars(pennies= 342, nickels=9, dimes=32, quarters=4)