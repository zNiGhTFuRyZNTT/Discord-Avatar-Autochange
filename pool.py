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
    'authorization': token,
    'content-type': 'application/json',
    'cookie': '__dcfduid=d5ac7780037911ee860a270012aff999; __sdcfduid=d5ac7781037911ee860a270012aff99944db6407de021dc56244a2334fdc5a7188b83ef4bc9252a81e53014f106e7076; _ga=GA1.1.1070393536.1685953234; locale=en-US; __cfruid=aa021c361df13c192fb1815457f780551fad45e6-1697863064; _cfuvid=.w6y8NJYdamBktBlKVzjv1Cba1BeOelY2256gCNer1o-1697863064975-0-604800000; cf_clearance=L_e4mMB_eQGyktrKthqyNk6tBa7z4mQG5pPLS72gm7c-1697863066-0-1-9b3d427f.db2f9ee4.fa1897ee-0.2.1697863066; _gcl_au=1.1.1201744322.1697863062; OptanonConsent=isIABGlobal=false&datestamp=Sat+Oct+21+2023+15%3A37%3A42+GMT%2B1100+(Australian+Eastern+Daylight+Time)&version=6.33.0&hosts=&landingPath=https%3A%2F%2Fdiscord.com%2F&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1; _ga_Q149DFWHT7=GS1.1.1697863062.3.0.1697863062.0.0.0',
    'origin': 'https://discord.com',
    'referer': 'https://discord.com/channels/@me',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.188 Safari/537.36',
    'x-debug-options': 'bugReporterEnabled',
    'x-discord-locale': 'en-US',
    'x-discord-timezone': 'Australia/Sydney',
    'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzExNi4wLjU4NDUuMTg4IFNhZmFyaS81MzcuMzYiLCJicm93c2VyX3ZlcnNpb24iOiIxMTYuMC41ODQ1LjE4OCIsIm9zX3ZlcnNpb24iOiIxMCIsInJlZmVycmVyIjoiaHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS8iLCJyZWZlcnJpbmdfZG9tYWluIjoid3d3Lmdvb2dsZS5jb20iLCJzZWFyY2hfZW5naW5lIjoiZ29vZ2xlIiwicmVmZXJyZXJfY3VycmVudCI6Imh0dHBzOi8vd3d3Lmdvb2dsZS5jb20vIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50Ijoid3d3Lmdvb2dsZS5jb20iLCJzZWFyY2hfZW5naW5lX2N1cnJlbnQiOiJnb29nbGUiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfYnVpbGRfbnVtYmVyIjoyMzkwMDQsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9'
    }
    response = requests.patch(url, headers=headers, data=payload)
    return response.text

if __name__ == '__main__':
    print("[>] Do not run this file directly")
