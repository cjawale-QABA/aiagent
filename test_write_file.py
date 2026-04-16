from functions.write_file import write_file
import unittest

class TestWriteFile(unittest.TestCase):

    def test_valid_update_write(self):
        result = write_file("calculator/", "lorem.txt", "Hello, World!")
        self.assertEqual(result, 'File "lorem.txt" written successfully.')

    def test_valid_new_write(self):
        result = write_file("calculator/", "pkg/moretext.txt", "pkg/test.txt says Hello, World!")
        self.assertEqual(result, 'File "pkg/moretext.txt" written successfully.')

    def test_valid_new_parent_write(self):
        result = write_file("calculator", "pkg2/text.txt", "lorem ipsum dolor sit amet")
        self.assertEqual(result, 'File "pkg2/text.txt" written successfully.')

    def test_invalid_directory(self):
        result = write_file("calculator/", "/temp/test.txt", "Hello, World!")
        self.assertEqual(result, 'Error: Cannot access "/temp/test.txt" as it is outside the permitted working directory')

    def test_write_to_directory(self):
        result = write_file("calculator/", "pkg/", "Hello, World!")
        self.assertEqual(result, 'Error: Cannot write to "pkg/" as it is a directory')

if __name__ == "__main__":
    unittest.main()