#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input("size"))

    arr = list(map(int, input("values").rstrip().split()))
    print(arr[::-1])
