import requests

def get_startup_data(api_key, startup_name):
    base_url = f"https://api.crunchbase.com/api/v4/"
    params = {
        "user_key": api_key,
        "name": startup_name
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        raise Exception(f"Failed to fetch data from Crunchbase API. Status code: {response.status_code}")


api_key = "bbd85a61b37f60b44fdf2ea6c9c364ab"
startup_name = "OpenAI"
startup_data = get_startup_data(api_key, startup_name)
print(startup_data)
