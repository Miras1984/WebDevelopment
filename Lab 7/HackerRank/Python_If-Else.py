#!/bin/python

import math
import os
import random
import re
import sys




if __name__ == '__main__':
    n = int(input())
    if n % 2 == 1: print('Weird')
    elif 2 <= n <= 5 and n % 2 == 0: print('Not Weird')
    elif n % 2 == 0 and 6 <= n <= 20: print('Weird')
    elif n > 20: print('Not Weird')