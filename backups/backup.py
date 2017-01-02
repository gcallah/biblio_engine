#!/usr/bin/env python3

"""
This file will contain the code to backup the Berkeley Bibliographic Engine for
any site.

Functions:

"""

import csv
import django.db


persons = [
              ['Maudud e Rabi', 'Syed', 'Student', 'Computer Science'],
              ['bin Hoq', 'Adnan', 'Student', 'Computer Science'],
              ['Callahan', 'Eugene', 'Faculty', 'Computer Science'],
          ]


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
            fwriter.writerow(record)


