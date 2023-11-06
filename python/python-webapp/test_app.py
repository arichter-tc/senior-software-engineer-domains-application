import unittest
from flask import Flask
from app import app  

class TestRandomQuoteAndPicture(unittest.TestCase):
    def test_display_random_quote_and_picture(self):
        tester = app.test_client(self)
        response = tester.get("/")
        status_code = response.status_code
        self.assertEqual(status_code, 200)

    def test_display_random_quote_and_picture_valid_key(self):
        tester = app.test_client(self)
        response = tester.get('/?key=123456')
        status_code = response.status_code
        self.assertEqual(response.status_code, 200)  

    def test_display_random_quote_and_picture_invalid_key(self):
        tester = app.test_client(self)
        response = tester.get('/?key=abs456')
        status_code = response.status_code
        self.assertEqual(response.status_code, 400)  

    def test_display_random_quote_and_picture_color(self):
        tester = app.test_client(self)
        response = tester.get('/')
        status_code = response.status_code
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(b'<img src="https://static.thenounproject.com/png/2347713-200.png">', response.data)

    def test_display_random_quote_and_picture_gray(self):
        tester = app.test_client(self)
        response = tester.get('/?grayscale')
        status_code = response.status_code
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(b'<img src="https://static.thenounproject.com/png/2347713-200.png">', response.data)

if __name__ == '__main__':
    unittest.main()