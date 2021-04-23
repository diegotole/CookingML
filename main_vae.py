from __future__ import absolute_import, division, print_function, unicode_literals


import tensorflow as tf

import os
import time
import numpy as np
import glob
import matplotlib.pyplot as plt
import PIL
import imageio

import csv, json, ast
from sklearn.preprocessing import MultiLabelBinarizer


from IPython import display

input_file = csv.DictReader(open("RAW_recipes.csv"))
ALL_INGR = []
for idx, line in enumerate(input_file):
    #     print(idx, line["ingredients"])
    #     print(type(line["ingredients"]))
    ALL_INGR.append(ast.literal_eval(line["ingredients"]))

print("last", ALL_INGR[-1])