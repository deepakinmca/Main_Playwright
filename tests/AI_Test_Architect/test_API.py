import pytest
import requests



@pytest.mark.api
def test_API():
    url = "https://jsonplaceholder.typicode.com/users/1"
    response = requests.get(url)
    print(response.status_code)
    print(response.json())
    