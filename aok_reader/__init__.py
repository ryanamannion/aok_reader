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
import ft


class Reader:
    """
    Handles reading of the corpus

    Attributes:
        path: str, path to top-level directory of AOK as downloaded

    Methods:
        load: loads all attributes from path
        load_master_csv: loads and returns master csv as free table
        index_master: returns dex indexed by given key
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
        Load all to class
        """
        self.master_csv = self.load_master_csv()

    def load_master_csv(self):
        """
        load master csv

        :return: list(dict), free table of master_csv, i.e. list of dictionaries
            with header row as keys and columns as values
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
        Use basic function of ft to index master free table

        Returns a dict of all observed values for that key, and each key points
        to each doc from self.master_csv with the key value for the specified
        field

        example: reader.index_master('Exclusivity-Answer') would return a dict
        with the keys True, False. Those keys point to each dict from the entire
        master_csv that had that value (i.e. True points to all docs that have
        true for that answer).

        :param index_by: str, one of the keys from master_csv (i.e. headers from
            master_clauses.csv)
        :return: dex indexed by specified value
        """
        return ft.indexBy(index_by, self.master_csv)
