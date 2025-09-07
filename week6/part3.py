# sort the dictionary based on the ages using lambda
students = [
    { 'name': "John", 'grade': "A",  'age': 20},
    { 'name': "Jane", 'grade': "B",  'age': 21},
    { 'name': "Joss", 'grade': "A+", 'age': 19},
    { 'name': "Jack", 'grade': "A-", 'age': 16},
    { 'name': "Dave", 'grade': "C",  'age': 25},
]
sort_result = sorted(students,key=lambda s:s['age'])
print(sort_result)
# sort by age (youngest -> oldest)