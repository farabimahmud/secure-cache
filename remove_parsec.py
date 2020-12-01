#!/bin/python3

import os
import glob

files = glob.glob("parsec_scripts/*.sh")

for f in files:
    os.remove(f)


