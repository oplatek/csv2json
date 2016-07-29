import unittest
import io
from . import convert
import json


class TestConvert(unittest.TestCase):

    def setUp(self):
        self.csv_input = '"column1","column2"\n"not_empty",""'
        self.delimiter = ','

    def test_simple(self):
        expected_output = [{'column1': 'not_empty', 'column2': ''}]
        csv_fp = io.StringIO(self.csv_input)
        json_fp = io.StringIO()
        convert(csv_fp, json_fp, delimiter=self.delimiter)
        converted_json_dct = json.loads(json_fp.getvalue()) 
        self.assertEqual(expected_output, converted_json_dct)
        json_fp.close()
        csv_fp.close()
