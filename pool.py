import base64
import json
import requests

class ConsoleColors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def to_base64(file_path):
    with open(f'./images/{file_path}', "rb") as img_file:
        encoded_data = base64.b64encode(img_file.read())
        return encoded_data

def change_avatar(image_file, token):
    image_data = to_base64(image_file).decode('utf-8')
      
    url = "https://discord.com/api/v9/users/@me"
    payload = json.dumps({'avatar': f'data:image/png;base64,{image_data}' })

    headers = {
        'authority': 'discord.com',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'authorization': token,  # Your authorization token here
        'content-type': 'application/json',
        'origin': 'https://discord.com',
        'referer': 'https://discord.com/channels/@me',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        # Add other necessary headers here
    }

    response = requests.patch(url, headers=headers, data=payload)
    return response.text

if __name__ == '__main__':
    print("[>] Do not run this file directly")
