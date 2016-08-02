import csv
from collections import namedtuple
try:
    from itertools import imap
except ImportError:  # Python 3
    imap = map


def write_csv(outfile, rows, delimiter=',', headers=[], encoding='utf-8'):
    """Creates a csv file with a given name from the given rows
    Args:
        string     outfile:    the file to writeout
        collection rows:       a collection of rows, each a collection
                               (eg, a list of lists)

        OPTIONAL:
        string      delimiter: the delimiter to use
        collection  headers:   a collection of identifiers to use as headers
        encoding    encoding:  the encoding to use on the file"""
    assert type(rows) is list or type(
        rows) is tuple, "Rows arg must be a list/tuple of either lists, tuples or dicts"
    assert len(rows), "Nothing to writeout"

    def write_dicts(outfile, rows, delimiter, headers, encoding):
        if not headers:
            headers = list(rows[0].keys())
        with open(outfile, 'w', encoding=encoding) as outfile:
            writer = csv.DictWriter(
                outfile, fieldnames=headers, delimiter=delimiter)
            writer.writeheader()
            writer.writerows(rows)

    def write_lists_tups_or_none(outfile, rows, delimiter, headers, encoding):
        with open(outfile, 'w', encoding=encoding) as outfile:
            writer = csv.writer(outfile, delimiter=delimiter)
            writer.writerow(headers) if headers else None
            writer.writerows(rows)

    if rows:
        if type(rows[0]) is dict:
            write_dicts(outfile, rows, delimiter, headers, encoding)
        else:
            write_lists_tups_or_none(
                outfile, rows, delimiter, headers, encoding)
    else:
        write_lists_tups_or_none(outfile, rows, delimiter, headers, encoding)


def read_csv(infile, delimiter=',', encoding='utf-8', named=False):
    """Reads a csv as a list of lists (unnamed) or a list of named tuples (named)
    Args:
        string   infile:    the file to read in
        string   delimiter: the delimiter used

        OPTIONAL:
        encoding encoding:  the encoding of the file
        boolean  named:     if true, loads rows as named tuples
                            (default lists)"""
    with open(infile, encoding=encoding) as f:
        reader = csv.reader(f, delimiter=delimiter)
        if named:
            headers = next(reader)
            # strip spaces and annoying things from headers
            names = [identifier.replace('-', '_').replace(' ', '_').lower()
                     for identifier in headers]
            Data = namedtuple("Data", names)
            named_rows = imap(Data._make, reader)
            return [row for row in named_rows]
        else:
            return list(list(row for row in reader))

# deprecated super-class


class jwcsv(object):

    def write_csv(self, outfile, rows, delimiter=',', headers=[], encoding='utf-8'):
        '''Basis for writing out csv in a subclass'''
        assert type(rows) is list or type(
            rows) is tuple, "Rows arg must be a list/tuple of either lists, tuples or dicts"
        assert len(rows), "Nothing to writeout"

        def write_dicts(outfile, rows, delimiter, headers, encoding):
            if not headers:
                headers = list(rows[0].keys())
            with open(outfile, 'w', encoding=encoding) as outfile:
                writer = csv.DictWriter(
                    outfile, fieldnames=headers, delimiter=delimiter)
                writer.writeheader()
                writer.writerows(rows)

        def write_lists_tups_or_none(outfile, rows, delimiter, headers, encoding):
            with open(outfile, 'w', encoding=encoding) as outfile:
                writer = csv.writer(outfile, delimiter=delimiter)
                writer.writerow(headers) if headers else None
                writer.writerows(rows)

        if rows:
            if type(rows[0]) is dict:
                write_dicts(outfile, rows, delimiter, headers, encoding)
            else:
                write_lists_tups_or_none(
                    outfile, rows, delimiter, headers, encoding)
        else:
            write_lists_tups_or_none(
                outfile, rows, delimiter, headers, encoding)

    def read_csv(self, infile, delimiter=',', encoding='utf-8', named=False):
        "Returns a list of lists (unnamed) or a list of named tuples (named)"
        with open(infile, encoding=encoding) as f:
            reader = csv.reader(f, delimiter=delimiter)
            if named:
                headers = next(reader)
                # strip spaces and annoying things from headers
                names = [identifier.replace('-', '_').replace(' ', '_').lower()
                         for identifier in headers]
                Data = namedtuple("Data", names)
                named_rows = imap(Data._make, reader)
                return [row for row in named_rows]
            else:
                return list(list(row for row in reader))