import pytest

@pytest.fixture
def browser(scope="session"):  #  module - для файла, function - для функций, session - один раз на все тесты
    print("Браузер стартует!")
    yield
    print("Браузер закрывается!")

@pytest.fixture
def chrome(browser):
    pass

@pytest.fixture
def user_id():
    return 123


def test_auth(user_id, chrome):
    assert user_id == 123