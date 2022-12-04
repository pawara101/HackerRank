#!/bin/python3

import math
import os
import random
import re
import sys
from traceback import print_tb



class Item:
    # Implement the Item here
    def __init__(self,name,price):
        self.name = name
        self.price = price


class ShoppingCart:
    def __init__(self):
        self.items = []

    def add(self,item):
        self.items.append(item)
        