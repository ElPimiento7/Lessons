import pytest


@pytest.fixture()
def seperator():
    print("=" * 10)
    yield "value"
    print("test finished")


@pytest.fixture(scope="session")
def all_tests():
    print("before all")
    yield
    print("after all")
