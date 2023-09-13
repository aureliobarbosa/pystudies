#!/usr/bin/env python3

# MAAB 2021-02-17 
# Tip for using booleans on argparse, from:
# https://stackoverflow.com/questions/15008758/parsing-boolean-values-with-argparse

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--feature', dest='feature', action='store_true')
parser.add_argument('--no-feature', dest='feature', action='store_false')
parser.set_defaults(feature=True)

args = parser.parse_args()

print(args)
