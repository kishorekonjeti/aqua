import pytest
from api_status_codes import *


def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="chrome,firefox,edge"
    )


@pytest.fixture(scope="class")
def getBrowserInfo(request):
    _browser = request.config.getoption("--browser")
    _browserheader = {"User-Agent": all_headers[_browser]}
    request.cls._browser = _browser
    request.cls._browserheader = _browserheader
    yield _browser
    # return _browser
