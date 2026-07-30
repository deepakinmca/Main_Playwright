import pytest
from playwright.sync_api import sync_playwright

@pytest.mark.api
def test_api_check():

    with sync_playwright() as p:

        request = p.request.new_context()

        response = request.get("https://opensource-demo.orangehrmlive.com")

        print(response.status)

        assert response.status == 200

        request.dispose()