from itertools import count

import numpy as np

sample = [0.0,5.2,3.1,0.0,12.4,0.0,7.5]

# Convert list to array
sampleArray = np.array(sample)
print("array:",sampleArray)

# Print total rainfall
sumResult = sampleArray.sum()
print("Total rainfall for the week:",sumResult)

# Print average rainfall for the week
averageResult = sampleArray.mean()
print("average rainfall for the week:",averageResult)

# Count days no rain
noRainDays = np.where(sampleArray == 0)
print("Count days no rain:",len(sampleArray[noRainDays]))

# Print days by index rain fall more than 5mm
print("more than 5mm",np.where(sampleArray>5)[0])

# more than 75 percentile data
result75 =  np.percentile(sampleArray,75)
print("more than 75 percentile",sampleArray[np.where(sampleArray>result75)])
print("more than 75 percentile",sampleArray[sampleArray>result75])