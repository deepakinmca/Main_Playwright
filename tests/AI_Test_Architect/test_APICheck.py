from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    request = p.request.new_context()

    response = request.get(
        "https://jsonplaceholder.typicode.com/users/1"
    )

    print(response.status)
    print(response.json())