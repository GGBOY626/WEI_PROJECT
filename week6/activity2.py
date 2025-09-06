data = ['a5', 'a2', 'b1', 'b3', 'c2']
sorted_data = sorted(data, key=lambda x: (x[0], int(x[1:])))
print(sorted_data)
# explain:['a2', 'a5', 'b1', 'b3', 'c2']
# because use x[0] to sort, is use ascil code
# if ascil code the same will sort by number
