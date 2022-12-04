import math
import os
import random
import re
import sys

def avg(*nums):

    total = 0
    for i in nums:
        total += i
        
    average = total/len(nums)
    average = "{:.2f}".format(average)

    print(average)

avg(2,3,4)
