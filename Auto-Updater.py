import os, zipfile, requests, shutil, io, json

GITHUB_REPO_OWNER = "AlexPT2k22"
GITHUB_REPO_NAME = "TestRepo"
GITHUB_API_URL = f'https://api.github.com/repos/{GITHUB_REPO_OWNER}/{GITHUB_REPO_NAME}'

def get_latest_version():
    response = requests.get(GITHUB_API_URL + '/releases/latest')
    if response.status_code == 200:
        print("Latest version found: " + response.json()['tag_name'])
        return response.json()['tag_name']
    elif response.status_code == 404:
        print("Latest version not found")
        return None

def get_user_app_version():
    with open(os.path.join(os.path.dirname(__file__), 'package.json')) as file:
        data = json.load(file)
        version = data['version']
        return version
    
def get_release_type():
    with open(os.path.join(os.path.dirname(__file__), 'package.json')) as file:
        data = json.load(file)
        release_type = data['release_type']
        return release_type
    
def get_asset_id():
    response = requests.get(GITHUB_API_URL + '/releases/latest')
    return response.json()['assets'][0]['id']

def update_user_app(latest_version, release_type):
    if release_type == "source_code":
        download_url = GITHUB_API_URL + '/zipball/' + latest_version
    elif release_type == "zip_archive":
        download_url = GITHUB_API_URL + '/releases/assets/133835650'
    else:
        print("Invalid release type specified in the configuration.")
        return

    response = requests.get(download_url, headers={'Accept': 'application/octet-stream'})

    if response.status_code != 200:
        print(f"Error downloading the latest release, does your release (.zip) exist?")
        return

    temp_dir = 'temp'
    os.makedirs(temp_dir, exist_ok=True)

    if release_type == "source_code":
        with zipfile.ZipFile(io.BytesIO(response.content)) as zip_file:
            zip_file.extractall(temp_dir)
    elif release_type == "zip_archive":
        zip_file_path = os.path.join(temp_dir, 'latest_release.zip')
        with open(zip_file_path, 'wb') as zip_file:
            zip_file.write(response.content)
    
    app_directory = os.path.dirname(__file__)

    if release_type == "source_code":
        for root, dirs, files in os.walk(temp_dir):
            for file in files:
                source_file = os.path.join(root, file)
                destination_file = os.path.join(app_directory, os.path.relpath(source_file, temp_dir))
                os.makedirs(os.path.dirname(destination_file), exist_ok=True)
                shutil.copy(source_file, destination_file)
    elif release_type == "zip_archive":
        with zipfile.ZipFile(zip_file_path, 'r') as zip_file:
            zip_file.extractall(app_directory)

    package_json_path = os.path.join(app_directory, 'package.json')
    with open(package_json_path, 'r') as file:
        data = json.load(file)
        data['version'] = latest_version

    with open(package_json_path, 'w') as file:
        json.dump(data, file, indent=4)

    shutil.rmtree(temp_dir)
    if release_type == "zip_archive" and os.path.exists(zip_file_path):
        os.remove(zip_file_path)

if __name__ == "__main__":
    asset_id = get_asset_id()
    release_type = get_release_type()
    latest_version = get_latest_version()
    user_app_version = get_user_app_version()
    if latest_version != user_app_version:
        print("New version available\nUpdating...")
        update_user_app(latest_version, release_type)
    else:
        print("You have the latest version installed")