import sys
import re
import numpy as np

input_list = []
init = True
for line in sys.stdin:
    if init:
        init = False
        N = int(line)  # first value is number of rows submitted
    else:
        if 'Exit' == line.rstrip():
            break
        input_list.append(line)

missing_idcs = np.zeros([20], dtype=int)
missing_vals = np.ones([20]) * -1
i = 0
for row_idx, row_val in enumerate(input_list):
    if 'Missing' in row_val:
        missing_idcs[i] = row_idx
        i += 1
    if i == 20:  # all missing values found
        break

def get_value(entry):
    pattern = r'\t(.*?)\n'
    match = re.search(pattern, entry)
    if match:
        return float(match.group(1))  # Return the captured substring
    return None

def nearest_fwd_val(idx, stock_list):
    for k in range(1, N - idx):
        neighbor_k = stock_list[idx + k]
        if 'Missing' in neighbor_k:
            if idx+k in missing_idcs:
                interpolation = missing_vals[np.where(missing_idcs == idx+k)][0]
                if interpolation != -1:  # default value is -1
                    return interpolation, k
            continue
        else:
            return get_value(neighbor_k), k

def nearest_bwd_val(idx, stock_list):
    for k in range(idx):
        neighbor_k = stock_list[idx - k]
        if 'Missing' in neighbor_k:
            if idx - k in missing_idcs:
                interpolation = missing_vals[np.where(missing_idcs == idx - k)][0]
                if interpolation != -1:  # default value is -1
                    return interpolation, k
            continue
        else:
            return get_value(neighbor_k), k

if missing_idcs[0] == 0: # first entry is missing
    missing_vals[0], _ = nearest_fwd_val(0, input_list)
if missing_idcs[-1] == N - 1:  # last entry is missing
    missing_vals[-1], _ = nearest_bwd_val(N - 1, input_list)

for i, miss_idx in enumerate(missing_idcs):
    if (i==0) or (i==19):  # first and last element have been treated above
        continue
    left_neighbor, left_distance = nearest_bwd_val(miss_idx, input_list)
    right_neighbor, right_distance = nearest_fwd_val(miss_idx, input_list)
    interpolation = right_neighbor + (left_neighbor - right_neighbor) / (left_distance + right_distance) * right_distance
    missing_vals[i] = interpolation


for val in missing_vals:
    print(val)
