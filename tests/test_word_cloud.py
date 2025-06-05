# Import library for testing
import unittest
from unittest.mock import patch, MagicMock
from cdstemplate import word_cloud

class TestGenerateWordCloud(unittest.TestCase):

    @patch("your_module.Path.glob")
    def test_generate_wordcloud(self, mock_glob):
        # Create a mock text file
        mock_file1 = MagicMock()
        mock_file1.read_text.return_value = "hello world"

        mock_file2 = MagicMock()
        mock_file2.read_text.return_value = "python programming"

        # Mock the .glob() call to return our mock files
        mock_glob.return_value = [mock_file1, mock_file2]

        # Call the function
        wc = word_cloud.generate_wordcloud("dummy_dir")

        # Assertions
        self.assertIn("hello", wc.words_)
        self.assertIn("python", wc.words_)





 