# Sort by age, then by salary if ages are the same
# use lambda
employees = [
    {'name': 'Alice',   'age': 30, 'salary': 80000},
    {'name': 'Bob',     'age': 25, 'salary': 50000},
    {'name': 'Charlie', 'age': 35, 'salary': 120000},
]
sort_result = sorted(employees,key=lambda s:(s['age'],s['salary']))
print(sort_result)

