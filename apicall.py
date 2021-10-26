import requests
import api_status_codes as SC


def doGet(url, headers):
    """
    This is a low level get method includes paramers , any other business logic which will require to run for all get calls
    """

    response = requests.get(url, headers=headers)

    return response.status_code


def doPost(url, headers):
    """
    This is a low level Post method includes paramers , any other business logic which will require to run for all Post calls
    """

    response = requests.post(url, headers=headers, data=None)

    return response.status_code
