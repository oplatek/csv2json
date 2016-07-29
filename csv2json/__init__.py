import csv
import json
import sys


def load_csv(fp_in, delimiter=',', quotechar='"', remove_empty=False, 
        fieldnames=None, **kwargs):
    r = csv.DictReader(fp_in, delimiter=delimiter, quotechar=quotechar, 
            fieldnames=fieldnames)
    rows = [row_dct for row_dct in r]
    if remove_empty:
        rows = [dict([(k, item) for k, item in row.items() if item]) for row in rows]
    return rows


def save_json(data, fp_out, pretty_spaces=4, sort_keys=False, **kwargs):
    json.dump(data, fp_out, indent=pretty_spaces, sort_keys=sort_keys)


def convert(csv, json, **kwargs):
    '''Convert csv to json.

    csv:  filename or file-like object
    json: filename  or file-like object


    if csv is '-' or None:
        stdin is used for input
    if json is '-' or None:
        stdout is used for output
    '''

    csv_local, json_local = None, None
    try:
        if csv == '-' or csv is None:
            csv = sys.stdin
        elif isinstance(csv, str):
            csv = csv_local = open(csv, 'r')

        if json == '-' or json is None:
            json = sys.stdout
        elif isinstance(json, str):
            json = json_local = open(json, 'w')

        data = load_csv(csv, **kwargs)
        save_json(data, json, **kwargs)
    finally:
        if csv_local is not None:
            csv_local.close()
        if json_local is not None:
            json_local.close()
