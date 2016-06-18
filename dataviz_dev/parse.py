"""
Data Visualization Project

Parse data from an ugly CSV or Excel file, and render it in
JSON, save to a database, and visualize in graph form.

Part I: Taking data from a CSV/Excel file, and return it into a format
that is easier for Python to play with.

Copyright (c) 2013 E. Lynn Root
Distributed under the zlib png license. See LICENSE for details.
"""

import csv
import pickle # (optional)

MY_FILE = "../dataviz/data/sample_sfpd_incident_all.csv"
OUT_FILE = './parse_output.txt'


def parse(raw_file, delimiter):
    '''Parses a raw CSV file to a JSON-like object'''
    
    # open CSV file
    opened_file = open(raw_file)
    
    # read CSV file
    csv_data = csv.reader(opened_file, delimiter=delimiter)
    
    # setup an empty list
    parsed_data = []
    
    # skip over first line for headers (column labels)
    fields = csv_data.next()
    
    # iterate over each row of the csv file, zip together field -> value
    for row in csv_data:
        parsed_data.append(dict(zip(fields, row)))
    
    # close the csv file
    opened_file.close()
    
    return parsed_data


def main():
    # Call our parse function and give it the needed parameters
    new_data = parse(MY_FILE, ',')
    
    # Let's see what the data looks like
    print new_data
    
    # (optional) open output .txt file
    out_file = open(OUT_FILE, 'w')
    
    # (optional) dump parsed_data structure to file
    pickle.dump(new_data, out_file)
    
    # (optional) close output file
    out_file.close()


if __name__ ==  '__main__':
    main()