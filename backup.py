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


persons = [
              ['Maudud e Rabi', 'Syed', 'Student', 'Computer Science'],
              ['bin Hoq', 'Adnan', 'Student', 'Computer Science'],
              ['Callahan', 'Eugene', 'Faculty', 'Computer Science'],
          ]

def read_records(tbl):
    subs = Subject.objects.all()
    for sub in subs:
        print(sub)
    return subs

def write_records(filenm, data):
    """
        Args:
            filenm: where to output the CSV
            data: what to output 
        Returns:
            None (for now: we probably want success or error codes)
    """
    with open(filenm, "w") as f_out:
        fwriter = csv.writer(f_out)
        for record in data:
            fwriter.writerow(str(record))

def main():
    recs = read_records("subject")
    write_records("test.csv", recs)

if __name__ == '__main__':
    main()
