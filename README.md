CSV to Json converter
=====================
![Travis CI badge for master branch](https://travis-ci.org/oplatek/csv2json.svg?branch=master)

Requires Python 3.4+

Install
-------
```
pip install csv2json
```

Usage
-----

From a command line

```
csv-to-json [-h] [--compact] [--csv_delimiter CSV_DELIMITER] 
            [--csv_quotechar CSV_QUOTECHAR] [--sort_keys]
            [--custom_headers CUSTOM_HEADERS [CUSTOM_HEADERS ...]] 
            [--remove_empty]
            csv_input json_output

```

A command line example

```
$ cat file.csv
a,b
1,"foo""bar"
2,baz
$ csv-to-json < file.csv
[
    {
        "a": "1",
        "b": "foo\"bar"
    },
    {
        "a": "2",
        "b": "baz"
    }
]
```

As a library

```python
from csv2json import convert, load_csv, save_json

with open('input.csv') as r, open('output.json', 'w') as w:
    convert(r, w)
```

Tests
-----
Run unittests e.g. by

    python3 setup.py test
