#!/usr/bin/env python
import sys

if len(sys.argv) != 2:
    print("Usage: %s <input_file>" % sys.argv[0])
    sys.exit(1)

with open(sys.argv[1]) as f:
    lines = f.readlines()
    sum = 0
    for line in lines:
        nums = []
        for char in line:
            if char.isdigit():
                nums.append(char)
        if nums:
            finalNums = int(nums[0] + nums[len(nums) - 1])
            sum += finalNums
    print(sum)
