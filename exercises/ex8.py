def c_to_f(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def f_to_c(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius


print(f_to_c(22))
print(c_to_f(-6))