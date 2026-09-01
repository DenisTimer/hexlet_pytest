from pathlib import Path
from hexlet_pytest import example


def get_test_data_path(filename):
    return Path(__file__).parent / "test_data" / filename


def read_file(filename):
    return get_test_data_path(filename).read_text()


def test_reverse():
    before = read_file("before.txt")
    excepted = read_file("after.txt")

    actual = example.reverse(before)

    assert actual == excepted