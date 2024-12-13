import os

import pytest
from solution import first_task, second_task


def test_first_task():
    input_file = os.path.join(os.path.dirname(__file__), "example.txt")
    input_data = list(map(lambda line: line.strip(), open(input_file, "r")))
    assert first_task(input_data) == 161


def test_second_task():
    input_file = os.path.join(os.path.dirname(__file__), "example.txt")
    input_data = list(map(lambda line: line.strip(), open(input_file, "r")))
    # print("INPUT DATA: ", input_data)
    input_data = [
        "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
    ]
    # input_file = os.path.join(os.path.dirname(__file__), "input.txt")
    # input_data = list(map(lambda line: line.strip(), open(input_file, "r")))

    # print("INPUT DATA: ", input_data)
    assert second_task(input_data) == 48
