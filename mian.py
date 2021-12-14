from dotenv import load_dotenv; load_dotenv()
from pool import cc, toB64, chAvatar # grab our funcs outta the pool.
import requests
import base64
import time
import json
import os

TIMEOUT = os.getenv('TIMEOUT') if len(os.getenv('TOKEN')) > 0 else 300
TOKEN = os.getenv('TOKEN') if len(os.getenv('TOKEN')) > 0 else False


images = os.listdir("./images/")
for image in images[:]:
  if not image.endswith((".png", "jpg", "ico", "jpeg", "gif")):
    images.remove(image)


def main():
  counter = 0
  while counter <= len(images):
    try:

      if counter == len(images)-1:

        chAvatar(images[counter], TOKEN)
        print(f"Changed to -> {images[counter]} - {counter}")
        counter = 0 
        time.sleep(TIMEOUT)

        continue

      else:

        chAvatar(images[counter], TOKEN)
        print(cc.OKGREEN + f"Changed to ->" + cc.ENDC+ cc.OKBLUE + f" '{images[counter]}' - number = {counter}" + cc.ENDC )
        counter += 1
        time.sleep(TIMEOUT)


    except Exception as e:
      print(e)
      time.sleep(10)
      continue


# <-- ---- --- Driver --- ---- -->
if __name__ == "__main__":
  print(cc.BOLD + cc.HEADER + "[>] Initializing ..." + cc.ENDC)
  # ----------------
  if not TOKEN:
    print(cc.WARNING + "[!] " + cc.ENDC + cc.FAIL +"You must provide a discord token in .env" + cc.ENDC)
    quit()
  elif TIMEOUT< 300:
    print(cc.WARNING + "[!] " + cc.ENDC + cc.FAIL +"Timeout must be more than 5mins = 300secs" + cc.ENDC)
    quit()
  # -----------------

  time.sleep(1)
  print("[>] Started !")
  print(cc.OKGREEN + f"All images -> "+ cc.ENDC+ cc.OKBLUE  + f"{images} count --> {len(images)}" + cc.ENDC)
  # ------------------
  main() #