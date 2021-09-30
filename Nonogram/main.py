import sys
import os
from pathlib import Path
from solver.nonogram import Nonogram
from tests.test_runner import TestExamples, TestMultisizeNanograms

BASE_DIR = os.path.dirname(Path(__file__).resolve())
sys.path.insert(0,BASE_DIR)

if __name__ == '__main__':
    runner = TestExamples()
    runner.run_all_tests()
    runner2 = TestMultisizeNanograms()
    runner2.test_all()
