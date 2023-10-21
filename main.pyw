from dotenv import load_dotenv
from pool import ConsoleColors as cc, change_avatar  # import functions from the pool module
import time
import os

load_dotenv()  # Load environment variables from .env file

INTERVAL = int(os.getenv('INTERVAL', '300'))  # Use a default value of 300 if INTERVAL is not set
TOKEN = os.getenv('TOKEN')

def get_images():
    image_extensions = ("png", "jpg", "ico", "jpeg", "gif", "webp")
    images = [image for image in os.listdir("./images/") if image.lower().endswith(image_extensions)]
    return images

images = get_images()

def main():
    if not TOKEN:
      print(cc.WARNING + "[!] " + cc.ENDC + cc.FAIL + "You must provide a discord token in .env" + cc.ENDC)
      return
      
    elif INTERVAL< 300:
      print(cc.WARNING + "[!] " + cc.ENDC + cc.FAIL +"INTERVAL must be more than 5mins = 300secs" + cc.ENDC)
      quit()

    if len(images) < 2:
      print(cc.WARNING + "[!] " + cc.ENDC + cc.FAIL + "You must provide at least 2 pictures in the 'images' directory" + cc.ENDC)
      return

    print(cc.BOLD + cc.HEADER + "[>] Initializing ..." + cc.ENDC)
    print("[>] Started!")
    print(cc.OKGREEN + f"All images -> " + cc.ENDC + cc.OKBLUE + f"{images} count --> {len(images)}" + cc.ENDC)

    with open('pid.txt', 'w') as pidf:
      pidf.write(str(os.getpid()))

    counter = 0
    while True:
        try:
            change_avatar(images[counter], TOKEN)
            print(cc.OKGREEN + f"Changed to ->" + cc.ENDC + cc.OKBLUE + f" '{images[counter]}' - number = {counter}" + cc.ENDC)
            counter = (counter + 1) % len(images)
            time.sleep(INTERVAL)

        except Exception as e:
            print(e)
            time.sleep(10)

if __name__ == "__main__":
    main()
