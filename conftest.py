import pytest

from helpers.generator import Generator


@pytest.fixture(scope="function")
def name():
    name = Generator().generate_random_string_name()
    return name


@pytest.fixture(scope="function")
def price():
    price = Generator().generate_random_float()
    return price
