import requests
import urllib.request
import json
from PIL import Image
from pyzbar.pyzbar import decode
import os
from dotenv import load_dotenv

load_dotenv()

os.getenv

token = os.getenv('token')

problem_url = requests.get('https://hackattic.com/challenges/reading_qr/problem?access_token=85a002e4a9ccf49c')

url = problem_url.json()['image_url']

qrcode = urllib.request.urlretrieve(url)
decodeQR = decode(Image.open(qrcode[0]))
qrdata = decodeQR[0].data.decode()

# payload = json.dumps({"code" : qrdata})
payload = {
    "code" : qrdata
}

solution = requests.post(
    f"https://hackattic.com/challenges/reading_qr/solve?access_token={token}", json=payload)

if solution.status_code == 200:
    print(f"Solution submitted successful - {solution.text}")
else:
    print(f"Something went wrong - {solution.text}")
