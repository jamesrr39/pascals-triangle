#!/env/bin/env python3

__author__ = 'james'


'''
script to print pascals triangle to a specified number of rows
for help, run
python cli-pascals-triangle.py -h
'''

import argparse
import triangle

parser = argparse.ArgumentParser(description='Print pascals triangle.')
parser.add_argument('max_row', metavar='max_row', type=int, help='highest row to print to.')
parser.add_argument('--print-all-rows', action='store_true', dest='print_all_rows', default=False, help='print all rows or just the last one?')

args = parser.parse_args()


zero_based_max_row = args.max_row - 1
for index, row_number in enumerate(range(0, args.max_row)):
    current_row = [1] if (0 == index) else triangle.get_next_row(current_row)
    if True == args.print_all_rows or index is zero_based_max_row:
        print current_row