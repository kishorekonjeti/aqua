from _pytest.mark import param
import pytest
from requests.api import request
import apicall

from api_status_codes import *


@pytest.mark.usefixtures("getBrowserInfo")
class TestApi:
    def test_print_browser_header(self, params=all_headers) -> None:
        """
        This is sample test method to print
        browser and its corresponding header
        """

        print("supplied browser name:", self._browser)
        print(f"Header for %s is %s" % (self._browser, self._browserheader))

    def test_doGet(self) -> None:
        """
        This is get REST api
        Returns success  if status code is 200
        """

        status_code = apicall.doGet(URL, self._browserheader)
        print("in do get:", status_code)
        assert status_code == API_SUCCESS

    def test_doPost(self) -> None:
        """
        This is Post  REST api
        expected result is fail as status code is not 200
        """
        status_code = apicall.doPost(URL, self._browserheader)
        assert status_code != API_SUCCESS
