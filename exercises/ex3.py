def add_numbers(array):
    total = 0.0
    for num in array:
        total += float(num)

    return total



array = [1.0, 1.1, "1"]
result = add_numbers(array)
print(result)