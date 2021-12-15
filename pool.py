import base64
import json
import requests


class cc:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def toB64(file):
    with open(f'./images/{file}', "rb") as img_file:
        kos =  base64.b64encode(img_file.read())
        return kos

def chAvatar(image, TOKEN):
  image = toB64(image).decode('utf-8')
      
  url = "https://discord.com/api/v9/users/@me"
  payload = json.dumps({'avatar': f"data:image/png;base64,{image}" })
  # print(image.decode('utf-8'))

  headers = {
    'Cookie': '__dcfduid=e4c3df3c85360215b6ba1f019af77369; _ga=GA1.2.528896288.1623296540; locale=en-US; __sdcfduid=00d74bf0034111ec958af99ca54ad1e440f7db87e754eb76a5220086bc6ce206440560151d00eb573f2ddbc4a1612fc8; _gcl_au=1.1.1933057783.1639226526; OptanonConsent=isIABGlobal=false&datestamp=Tue+Dec+14+2021+22%3A04%3A03+GMT%2B1100+(Australian+Eastern+Daylight+Time)&version=6.17.0&hosts=&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1&AwaitingReconsent=false; _gid=GA1.2.42709606.1639479844',
    'Authorization': TOKEN,
    'Content-Type': 'application/json',
    'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36",
    'X-Super-Properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzk1LjAuNDYzOC42OSBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiOTUuMC40NjM4LjY5Iiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiJodHRwczovL3d3dy5nb29nbGUuY29tLyIsInJlZmVycmluZ19kb21haW4iOiJ3d3cuZ29vZ2xlLmNvbSIsInNlYXJjaF9lbmdpbmUiOiJnb29nbGUiLCJyZWZlcnJlcl9jdXJyZW50IjoiaHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS8iLCJyZWZlcnJpbmdfZG9tYWluX2N1cnJlbnQiOiJ3d3cuZ29vZ2xlLmNvbSIsInNlYXJjaF9lbmdpbmVfY3VycmVudCI6Imdvb2dsZSIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjEwODA0NCwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0='
  }

  response = requests.request("PATCH", url, headers=headers, data=payload)
  return response.text

if __name__ == '__main__':
  print("[>] Do not run this file Directly")