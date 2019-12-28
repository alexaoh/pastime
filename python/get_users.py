import requests

def get_users_and_return_reversed(url):
    """Gets user list from API-endpoint and returns a reversed user list

    Input: url
    Output: reversed user list

    """

    r = requests.get(url)

    if r:
        r_list = r.json()
        r_list.reverse()
        return r_list


