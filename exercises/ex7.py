def calc_total(array, tax):
    total=0
    tax = float(tax.strip('%'))
    for i in array:

        total += float(i)+(float(i)*(tax/100))
    print(total)

array = [2.00, 4.00, 4.00]
tax = "10%"
result = calc_total(array, tax)
print(result)