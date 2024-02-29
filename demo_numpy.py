import numpy as np

height = [125,145,210]
weight = [124,522,541]

np_height = np.array(height)


np_height_m = np_height / 100
print(np_height_m)


np_weight_kg = np.array(weight) * 0.453592
bmi = np_weight_kg / np_height_m ** 2
print(bmi)

print("Median: " + str(np.median(np_height)))