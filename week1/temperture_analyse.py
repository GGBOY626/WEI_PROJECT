import numpy as np;

# average
temp= [18.5,19,20,25.0,2,30,13.9]
total = 0
i = 0
for e in temp:
    total = total+ e
    i = i + 1
aver = (total / i)
print(aver)
arr = np.array(temp)
aver2 = np.mean(arr)
print( "Average temperture:", aver2)

# highest lowest
highest_tem = np.max(arr)
lowest_tem = np.min(arr)
print("highest_tem:",highest_tem,"lowest_tem:",lowest_tem)

# Convert all temperatures to Fahrenheit
fahrenheit = arr * 9 / 5 + 32
print(fahrenheit)

# Identify and print the indices of days where the temperature exceeded 20°C.
for e in temp:
    if e > 20:
        print(e)
print("the temperature exceeded 20°C:",arr[np.where(arr>20)])