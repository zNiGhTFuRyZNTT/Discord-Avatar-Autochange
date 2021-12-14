from dotenv import load_dotenv; load_dotenv()
import requests
import base64
import time
import json
import os

SEC_BETWEEN_EACH_ = 50

images = os.listdir("./images/")
for image in images[:]:
  if not image.endswith((".png", "jpg", "ico", "jpeg", "gif")):
    images.remove(image)


def toB64(file):
    with open(f'./images/{file}', "rb") as img_file:
        kos =  base64.b64encode(img_file.read())
        return kos

def chAvatar(image):
  image = toB64(image).decode('utf-8')
      
  url = "https://discord.com/api/v9/users/@me"
  payload = json.dumps({'avatar': f"data:image/png;base64,{image}" })
  # print(image.decode('utf-8'))

  headers = {
    'Cookie': '__dcfduid=304b98c159c411ecb8a042010a0a06bd',
    'Authorization': os.getenv('TOKEN'),
    'Content-Type': 'application/json',
    'X-Super-Properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzk1LjAuNDYzOC42OSBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiOTUuMC40NjM4LjY5Iiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiJodHRwczovL3d3dy5nb29nbGUuY29tLyIsInJlZmVycmluZ19kb21haW4iOiJ3d3cuZ29vZ2xlLmNvbSIsInNlYXJjaF9lbmdpbmUiOiJnb29nbGUiLCJyZWZlcnJlcl9jdXJyZW50IjoiaHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS8iLCJyZWZlcnJpbmdfZG9tYWluX2N1cnJlbnQiOiJ3d3cuZ29vZ2xlLmNvbSIsInNlYXJjaF9lbmdpbmVfY3VycmVudCI6Imdvb2dsZSIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjEwODA0NCwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0='
  }

  response = requests.request("PATCH", url, headers=headers, data=payload)
  return response.text

def main():
  counter = 0
  while counter <= len(images):
    try:

      if counter == len(images)-1:

        chAvatar(images[counter])
        print(f"Changed to -> {images[counter]} - {counter}")
        counter = 0 
        time.sleep(SEC_BETWEEN_EACH_)

        continue

      else:

        chAvatar(images[counter])
        print(f"Changed to -> {images[counter]} - {counter}")
        counter += 1
        time.sleep(SEC_BETWEEN_EACH_)


    except Exception as e:
      print(e)
      pass



if __name__ == "__main__":
  print("[>] Initializing ...")
  time.sleep(1)
  print("[>] Started !")
  print(f"All images -> {images} count --> {len(images)}")
  main()