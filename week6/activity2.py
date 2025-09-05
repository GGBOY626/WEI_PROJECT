# use enumerate() for looping to add 5 extra point to each grade in the list, the 5th one add 10
grades = [88, 92, 78, 65, 50, 94]
for i,grade in enumerate(grades):
    if i == 4:
        grades[i] += 10
    else:
        grades[i] += 5

# filter out elements depend on their index:
# use list comprehension and enumerate() to get elements with even index
data = [100, 200, 300, 400, 500]
result = [v for i,v in enumerate(data) if i%2==0]
print(result)

# create a dictionary from lists using zip()
keys = ['name', 'age', 'grade']
values = ['Alice', 25, 'A']
result2 = dict(zip(keys,values))
print(result2)
