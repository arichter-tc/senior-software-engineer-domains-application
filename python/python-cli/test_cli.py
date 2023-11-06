import unittest
from cli import get_quote, get_picture

class TestGetQuote(unittest.TestCase):
    def test_get_quote_valid_key(self):
       
        self.assertIsInstance(get_quote(key="123456"), str)
        self.assertNotEqual(get_quote(key="123456"), "Failed to fetch a quote.")
    
    def test_get_quote_invalid_key(self):
        with self.assertRaises(ValueError) as context: 
            get_quote(key="abc123")
            get_quote(key=".")
            get_quote(key="reason")
            get_quote(key="$!@#%^&*(*)")

    def test_get_quote_no_key(self):
        self.assertIsInstance(get_quote(), str)
        self.assertNotEqual(get_quote(), "Failed to fetch a quote.")
        
class TestGetPicture(unittest.TestCase):

    def test_get_picture(self):
        self.assertIsInstance(get_picture(), str)
        self.assertNotEqual(len(get_picture()), 0)
        ansi_pattern = r'(\[.*\])*'
        self.assertRegex(get_picture(), ansi_pattern)

    def test_get_picture_grayscale(self):
        self.assertIsInstance(get_picture(grayscale=True), str)
        self.assertNotEqual(len(get_picture(grayscale=True)), 0)
        ansi_pattern = r'(\[.*\])*'
        self.assertRegex(get_picture(), ansi_pattern)


if __name__ == '__main__':
    unittest.main()
