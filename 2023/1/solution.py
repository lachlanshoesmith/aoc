#!/usr/bin/env python
import sys

if len(sys.argv) != 2:
    print("Usage: %s <input_file>" % sys.argv[0])
    sys.exit(1)

with open(sys.argv[1]) as f:
    lines = f.readlines()
    sum = 0
    strings = [['nine', 'n9e'], ['eight', 'e8t'], ['seven', 's7n'], ['six', 's6x'], [
        'five', 'f5e'], ['four', 'f4r'], ['three', 't3e'], ['two', 't2o'], ['one', 'o1e']]
    for line in lines:
        nums = []
        for i, num in enumerate(strings):
            if num[0] in line:
                line = line.replace(strings[i][0], strings[i][1])
        for char in line:
            if char.isdigit():
                nums.append(char)
        if nums:
            finalNums = int(nums[0] + nums[len(nums) - 1])
            sum += finalNums
    print(sum)
