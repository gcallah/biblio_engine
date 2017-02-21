#!/usr/bin/env python3

"""
This file will contain the code to backup the Berkeley Bibliographic Engine for
any site.

Functions:

"""

import csv
import django
django.setup()
from berkeley.models import *


def read_records(tbl):
    recs = tbl.objects.values()
    # lines 20-22 are just for debugging:
    for rec in recs:
        for (key, val) in rec.items():
            print(key + ": " + str(val))
    return recs

def write_records(filenm, recs):
    """
        Args:
            filenm: where to output the CSV
            recs: the data to output 
        Returns:
            None (for now: we probably want success or error codes)
    """
    with open(filenm, "w") as f_out:
        fwriter = csv.writer(f_out)
        for record in recs:
            output = []
            for (key, val) in record.items():
                print("Val = " + str(val))
                output.append(val)
            fwriter.writerow(output)

def main():
    recs = read_records(Journal)
    write_records("test.csv", recs)

if __name__ == '__main__':
    main()
