from dotenv import load_dotenv; load_dotenv()
from pool import cc, chAvatar # grab our funcs outta the pool.
import time
import os

INTERVAL = int(os.getenv('INTERVAL')) if len(os.getenv('INTERVAL')) > 0 else 300
TOKEN = os.getenv('TOKEN') if len(os.getenv('TOKEN')) > 0 else False

def get_images():
  images = os.listdir("./images/")
  for image in images[:]:
    if not image.endswith(("png", "jpg", "ico", "jpeg", "gif")):
      images.remove(image)
  return images
images = get_images()

def main():
  counter = 0
  while counter <= len(images):
    try:

      if counter == len(images)-1:

        chAvatar(images[counter], TOKEN)
        print(f"Changed to -> {images[counter]} - {counter}")
        counter = 0 
        time.sleep(INTERVAL)

        continue

      else:

        chAvatar(images[counter], TOKEN)
        print(cc.OKGREEN + f"Changed to ->" + cc.ENDC+ cc.OKBLUE + f" '{images[counter]}' - number = {counter}" + cc.ENDC )
        counter += 1
        time.sleep(INTERVAL)


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
  elif INTERVAL< 300:
    print(cc.WARNING + "[!] " + cc.ENDC + cc.FAIL +"INTERVAL must be more than 5mins = 300secs" + cc.ENDC)
    quit()
  # -----------------
  if len(images) < 1:
    print(cc.WARNING + "[!] " + cc.ENDC + cc.FAIL +"You Provide at least 2 pictures in 'images' directory" + cc.ENDC)
    quit()

  time.sleep(1)
  print("[>] Started !")
  print(cc.OKGREEN + f"All images -> "+ cc.ENDC+ cc.OKBLUE  + f"{images} count --> {len(images)}" + cc.ENDC)
  # ------------------
  # create a file and write the process id into it so we can terminate later.
  with open('pid.txt', 'w') as pidf:
    pidf.write(str(os.getpid()))
  pidf.close()
  # ----------------
  main() #