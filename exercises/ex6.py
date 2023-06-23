def slice_it(array):

    sliced_array=""
    for str in array:
        sliced_array+=str[:2]
    print(sliced_array)


array = ["this", "is", "another", "test"]
r = slice_it(array)
print(r)