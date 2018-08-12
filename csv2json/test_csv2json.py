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


class TestCustomHeaders(unittest.TestCase):
    def setUp(self):
        self.csv_input = '"value1","value2"\n"value3","value4"'
        self.custom_headers= ["column1", "column2"]
        self.delimiter = ','

    def test_insert_headers(self):
        expected_output = [{'column1': 'value1', 'column2': 'value2'}, {'column1': 'value3', 'column2': 'value4'}]
        csv_fp = io.StringIO(self.csv_input)
        json_fp = io.StringIO()
        convert(csv_fp, json_fp, delimiter=self.delimiter, custom_headers=self.custom_headers)
        converted_json_dct = json.loads(json_fp.getvalue())
        self.assertEqual(expected_output, converted_json_dct)
        json_fp.close()
        csv_fp.close()
