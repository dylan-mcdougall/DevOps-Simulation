import unittest
from main import parse_data, celsius_to_fahrenheit

class TestMain(unittest.TestCase):
    """Test proper functionality of key functions"""
    def test_parse_data(self):
        """Test ability for json to parse altering data"""
        json = [
            {
                "sensors": [
                    {"title": "temperature", "lastMeasurement": {"value": "25"}},
                    {"title": "humidity", "lastMeasurement": {"value": "60"}}
                ]
            },
            {
                "sensors": [
                    {"title": "Temperature", "lastMeasurement": {"value": "30"}},
                    {"title": "pressure", "lastMeasurement": {"value": "100"}}
                ]
            },
            {
                "sensors": [
                    {"title": "Temperature"},
                    {"title": "humidity"}
                ]
            }
        ]

        expected_output = ["25", "30"]
        self.assertEqual(parse_data(json), expected_output)

    def test_celsius_to_fahrenheit(self):
        """Test proper value conversion to fahrenheit"""
        temp_list = ["10", "20", "30"]
        expected_avg = '57.71'
        self.assertEqual(celsius_to_fahrenheit(temp_list), expected_avg)

if __name__ == '__main__':
    unittest.main()
