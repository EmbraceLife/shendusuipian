import os
import unittest

def analyze_text(filename):
    with open(filename, 'r') as f:
        return sum(1 for _ in f)

class TextAnalysisTests(unittest.TestCase):
    """Tests for the `analyze_text()` function"""

    def setUp(self):
        """Fixture that create a file for the next methods to use"""
        self.filename = "text_analysis_test_file.txt"
        with open(self.filename, 'w') as f:
            f.write("Python is a great tool")
    def tearDown(self):
        """fixture that deletes the files used by the test methods"""
        try:
            os.remove(self.filename)
        except:
            pass

    def test_function_runs(self):
        """Basic smoke test: does the function run."""
        analyze_text(self.filename)

    def test_line_count(self):
        """check that the line count is correct"""
        self.assertEqual(analyze_text(self.filename), 1)


if __name__ == "__main__":
    unittest.main()

dir(unittest)

dir(unittest.TestCase)
