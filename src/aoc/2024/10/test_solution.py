import os

import pytest
from solution import first_task, second_task


def test_first_task():
    input_file = os.path.join(os.path.dirname(__file__), "example.txt")
    input_data = list(map(lambda line: line.strip(), open(input_file, "r")))
    assert first_task(input_data) == 1

    input_file = os.path.join(os.path.dirname(__file__), "example2.txt")
    input_data = list(map(lambda line: line.strip(), open(input_file, "r")))
    assert first_task(input_data) == 36


def test_second_task():
    input_file = os.path.join(os.path.dirname(__file__), "example2.txt")
    input_data = list(map(lambda line: line.strip(), open(input_file, "r")))
    assert second_task(input_data) == 81
