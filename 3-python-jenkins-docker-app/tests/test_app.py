import unittest
from app import main

class TestApp(unittest.TestCase):
    def test_main_runs(self):
        # This test just checks if the main function runs without error
        main()

if __name__ == '__main__':
    unittest.main()
