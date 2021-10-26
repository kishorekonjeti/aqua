import requests
import api_status_codes as SC


def doGet(url, headers)->None:
    """
    This is a low level get method includes paramers , any other business logic which will require to run for all get calls
    """
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        return response.status_code



    except requests.exceptions.HTTPError as errh:
        print(errh)
    except requests.exceptions.ConnectionError as errc:
        print(errc)
    except requests.exceptions.Timeout as errt:
        print(errt)
    except requests.exceptions.RequestException as err:
        print(err)

   


def doPost(url, headers)->None:
    """
    This is a low level Post method includes paramers , any other business logic which will require to run for all Post calls
    """
    try:
        response = requests.post(url, headers=headers, data=None)
        response.raise_for_status()

        return response.status_code
    
    except requests.exceptions.HTTPError as errh:
        print(errh)
    except requests.exceptions.ConnectionError as errc:
        print(errc)
    except requests.exceptions.Timeout as errt:
        print(errt)
    except requests.exceptions.RequestException as err:
        print(err)
