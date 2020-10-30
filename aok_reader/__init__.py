#!/usr/bin/env python3
"""
aok_reader/__init__.py

By Ryan A. Mannion
ram321@georgetown.edu
twitter @ryanamannion

A package to manage reading and loading the AOK dataset into python objects

Assumes the top-level dir is as initially downloaded

By "as initially downloaded" I mean when you unarchive the zip file, direct the
reader to the resulting directory. As of the beta, this includes:
    - full_contracts/     # contains full contract pdf files
    - individual_contract_clauses/    # contains relevant clauses
    - master_clauses.csv
    and some other information about the corpus

basic usage:

>>> import aok_reader
>>> path = 'path/to/aok/download/dir/'
>>> reader = aok_reader.Reader(path=path)
>>> reader.load()
>>> # and you're off to the races
"""

import csv
import glob
import ft
import sys


class Reader:
    """
    Handles reading of the corpus

    Attributes:
        path: str, path to top-level directory of AOK as downloaded

    """

    def __init__(self, path):
        """
        Initialize with path to top-level dir

        :param path: str, path to top-level AOK dir
        """
        if not path.endswith('/'):
            path = path + '/'
        self.path = path
        self.master_csv = None

    def load(self):
        """
        Load all
        :return:
        """
        master_csv = self.load_master_csv()

    def load_master_csv(self):
        """
        load master csv

        :param path: str, path to top-level corpus directory
        :param generator: bool, if True loads master csv as a generator, else
            load it all at once
        :return: TODO
        """

        path_to_master_csv = self.path + 'master_clauses.csv'

        entire_sheet = []
        with open(path_to_master_csv, 'r') as fstream:
            rows = csv.reader(fstream, delimiter=',', quotechar='"')
            for i, row in enumerate(rows):
                if i == 0:
                    headers = row       # store headers
                    continue
                else:       # make a free table of the master csv
                    # want to change some values to make it more python friendly
                    new_row = []
                    for cell in row:
                        if cell == '':
                            new_row.append(None)
                        elif '\n\n' in cell:
                            # multiple items, split and store as list
                            new_row.append(cell.split('\n\n'))
                        elif cell.lower() == 'yes':
                            new_row.append(True)
                        elif cell.lower() == 'no':
                            new_row.append(False)
                        else:
                            new_row.append(cell)

                    doc = dict(zip(headers, new_row))
                    entire_sheet.append(doc)

        self.master_csv = entire_sheet
        return entire_sheet

    def index_master(self, index_by):
        """
        Use basic function of ft to index master free table by index_by
        :param index_by:
        :return:
        """
        return ft.indexBy(index_by, self.master_csv)
