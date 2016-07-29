CSV to Json converter
=====================

Requires Python 3.4+

Install
-------
```
pip install cvs2json
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


As a library

```python
from csv2json import convert, load_csv, save_json

with open('input.csv') as r, open('output.json', 'w') as w:
    convert(r, w)
```
