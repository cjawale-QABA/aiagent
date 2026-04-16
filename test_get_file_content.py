import functions.get_file_content
import unittest

class TestGetFileContent(unittest.TestCase):

    def test_valid_lorem(self):
        result = functions.get_file_content.get_file_content("calculator/", "lorem.txt")
        self.assertIn("truncated at", result)
        self.assertTrue(len(result) > 10000)
        self.assertIsInstance(result, str)

    def test_valid_file(self):
        result = functions.get_file_content.get_file_content("calculator/", "pkg/calculator.py")
        self.assertTrue(len(result) < 10000)
        self.assertIsInstance(result, str)

    def test_outside_directory(self):
        result = functions.get_file_content.get_file_content("calculator/", "/bin/cat")
        self.assertIn("Error:", result)
        self.assertIn("outside the permitted working directory", result)
    
    def test_invalid_file(self):
        result = functions.get_file_content.get_file_content("calculator/", "pkg/does_not_exist.py")
        self.assertIn("Error:", result)

if __name__ == "__main__":
    unittest.main()
