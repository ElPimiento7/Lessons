import pytest
import allure
from Lessons.calculator import calculator


@allure.feature("Calculator")
@allure.story("Plus")
def test_plus():
    assert calculator("2+2") == 4


@allure.feature("Calculator")
@allure.story("No signs")
def test_no_signs():
    with pytest.raises(ValueError) as error:
        calculator("abracadabra")
    assert "Выражение должно содержать хотя бы один знак (+-/*)" == error.value.args[0]


@allure.feature("Calculator")
@allure.story("Two signs")
def test_two_signs():
    with pytest.raises(ValueError) as error:
        calculator("2+2+2")
    assert "Выражение должно содержать 2 целых числа и 1 знак)" == error.value.args[0]


if __name__ == '__main__':
    pytest.main()
