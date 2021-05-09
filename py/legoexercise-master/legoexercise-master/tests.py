import pytest
from jobs import get_mean, get_median


@pytest.fixture
def ten_numbers_list():
    return [50, 60, 70, 20, 10, 40, 80, 10, 90, 70]


@pytest.fixture
def twenty_numbers_list():
    return [4, 16, 88, 15, 12, 60, 99, 92, 68, 53,
            22, 44, 56, 75, 73, 24, 10, 8, 61, 77]


def test_get_mean(twenty_numbers_list):
    assert get_mean(twenty_numbers_list) == 47.85


def test_get_median(ten_numbers_list):
    assert get_median(ten_numbers_list) == 55
