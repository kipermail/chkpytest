import pytest

from faker import Faker
from random import randint
from src.generators.player import Player


@pytest.fixture(scope="function")
def say_hello():
    print("Hello")

@pytest.fixture
def make_random_number():
    res = randint(1, 100)
    print("Make random number", res)
    yield res
    print("\n", "Used random number", res)

@pytest.fixture
def create_fake_user():
    fake_user = Faker()
    return {
        "name": fake_user.first_name(),
        "surname": fake_user.last_name(),
        "email": fake_user.email(),
        "phone_number": fake_user.phone_number(),
        "address": fake_user.address()
    }

def _calculate(x, y):
    return x + y

@pytest.fixture
def calculate():
    return _calculate


@pytest.fixture
def get_player_generator():
    return Player()