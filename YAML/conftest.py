import pytest


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", help="input browsername")
    parser.addoption("--headless", action="store", help="input headless")
    parser.addoption("--initial_url", action="store", help="input initialUrl")

@pytest.fixture
def params(request):
    params = {}
    browserAssign = request.config.getoption('--browser')  
    params['browser'] = browserAssign if (browserAssign != None) else 'chrome'
    params['headless'] = request.config.getoption('--headless')
    params['initial_url'] = request.config.getoption('--initial_url')

    return params