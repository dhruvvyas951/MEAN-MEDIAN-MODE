# imports
import csv
from collections import Counter

# local data
with open('Graph Visualization/Height-Weight.csv', newline = '') as f:
    reader = csv.reader(f)
    file_data = list(reader)

file_data.pop(0)
new_data = []

for i in range(len(file_data)):
    n_num = file_data[i][1]
    new_data.append(float(n_num))

n = len(new_data)
total = 0

# for mean
for x in new_data:
    total += x

mean = total / n

# for median
if n % 2 == 0:
    median1 = float(new_data[n//2])
    median2 = float(new_data[n//2 - 1])
    median = (median1 + median2)/2

else:
    median = new_data[n//2]
    print(n)

# for mode
data  = Counter(new_data)
mode_data_range = {
    '50-60': 0,
    '60-70': 0,
    '70-80': 0
}
for height, occurrence in data.items():
    if 50 < float(height) < 60:
        mode_data_range['50-60'] += occurrence 
    
    elif 60 < float(height) < 70:
        mode_data_range['60-70'] += occurrence 
    
    elif 70 < float(height) < 80:
        mode_data_range['70-80'] += occurrence 

mode_range, mode_occurrence = 0,0

for range, occurrence in mode_data_range.items():
    if occurrence > mode_occurrence:
        mode_range, mode_occurrence = [int(range.split('-')[0]), int(range.split('-')[1])], occurrence
        mode = float((mode_range[0] + mode_range[1])/2)

# results
print('Mean -> ' + str(mean))
print("Median -> " + str(median))
print(f"Mode -> {mode: 2f}")