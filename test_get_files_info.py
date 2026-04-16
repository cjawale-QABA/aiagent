import functions.get_files_info
import unittest

class TestGetFilesInfo(unittest.TestCase):

    def test_valid_no_target_directory(self):
        result = functions.get_files_info.get_files_info("calculator/")
        self.assertIn(" - tests.py: - file_size:", result)
        self.assertIn(" - main.py: - file_size:", result)
        self.assertIn(" - pkg: - file_size:", result)

    def test_valid_directory(self):
        result = functions.get_files_info.get_files_info("calculator/", "pkg")
        self.assertIn(" - render.py: - file_size:", result)
        self.assertIn(" - __pycache__: - file_size:", result)
        self.assertIn(" - calculator.py: - file_size:", result)

    def test_invalid_directory(self):
        result = functions.get_files_info.get_files_info("calculator/", "invalid_dir")
        self.assertEqual(result, 'Error: "invalid_dir" is not a valid directory.')

    def test_outside_permitted_directory(self):
        result = functions.get_files_info.get_files_info("calculator/", "../")
        self.assertEqual(result, 'Error: Cannot list "../" as it is outside the permitted working directory')

if __name__ == "__main__":
    unittest.main()