import pytest
import allure


@allure.feature("Experiments")
@allure.story("One is one")
@pytest.mark.smoke
def test_one_is_one(seperator):
    print(seperator)
    assert 1 == 1


@allure.feature("Experiments")
@allure.story("Two is two")
@pytest.mark.smoke
def test_two_is_two(all_tests):
    assert 2 == 2


@allure.feature("Experiments")
@allure.story("Three is three")
@pytest.mark.smoke
@pytest.mark.skip("Bug #42")
def test_three_is_three(seperator):
    assert 3 == 2
