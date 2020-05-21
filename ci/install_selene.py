import requests
import json
import zipfile
import os
import subprocess

LATEST_RELEASES_ENDPOINT = "https://api.github.com/repos/Kampfkarren/selene/releases/latest"
DOWNLOAD_DIR = "/tmp/selene/bin"

def install_selene():
	print("Fetching latest release info...")
	res = requests.get(LATEST_RELEASES_ENDPOINT)
	res.raise_for_status()
	body = res.json()
	asset = list(filter(lambda asset: asset["name"] == "selene-linux", body["assets"]))[0]
	url = asset["browser_download_url"]
	print("Downloading latest release...")
	file = requests.get(url, stream=True)
	os.makedirs(DOWNLOAD_DIR, exist_ok=True)
	file_name = os.path.join(DOWNLOAD_DIR, "selene")
	with open(file_name, "wb") as f:
		f.write(file.content)
	os.chmod(file_name, 755)
	print("Downloaded")
	print("Test selene 2")
	subprocess.check_call(f"{file_name} --version", stdout=subprocess.STDOUT, stderr=subprocess.STDOUT, shell=True)

if __name__ == "__main__":
	install_selene()