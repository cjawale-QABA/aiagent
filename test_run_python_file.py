from functions.run_python_file import run_python_file
import unittest

class TestRunPythonFile(unittest.TestCase):

    def test_invalid_non_python_file(self):
        result = run_python_file("calculator", "lorem.txt")
        self.assertEqual(result, 'Error: "lorem.txt" as it is not a Python file')

    def test_valid_main(self):
        result = run_python_file("calculator", "main.py")
        self.assertIn("STDOUT: ", result)
        self.assertIn('Usage: python main.py "<expression>"', result)

    def test_valid_command(self):
        result = run_python_file("calculator", "main.py", ["3 + 5"])
        self.assertIn("STDOUT: ", result)
        self.assertIn("8", result)

    def test_valid_test_file(self):
        result = run_python_file("calculator", "tests.py")
        self.assertIn("STDOUT: ", result)
        self.assertIn('Ran 9 tests in', result)

    def test_invalid_non_permitted_work_dir_file(self):
        result = run_python_file("calculator", "../main.py")
        self.assertEqual(result, 'Error: Cannot access "../main.py" as it is outside the permitted working directory')

    def test_invalid_nonexistent_file(self):
        result = run_python_file("calculator", "nonexistent.py")
        self.assertEqual(result, 'Error: Cannot run "nonexistent.py" as it is not a file')

if __name__ == "__main__":
    unittest.main()