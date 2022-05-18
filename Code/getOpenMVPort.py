import os
device:str  = ""

if os.name == 'nt':  # sys.platform == 'win32':
    from serial.tools.list_ports_windows import comports
elif os.name == 'posix':
    from serial.tools.list_ports_posix import comports
else:
    raise ImportError("Sorry: no implementation for your platform ('{}') available".format(os.name))

iterator = sorted(comports(False))
for n, (port, desc, hwid) in enumerate(iterator, 1):
    if desc.replace(f" ({port})", "") == "OpenMV Cam USB COM Port":
        print("Open MV")
        device: str = port
    # OpenMV Cam USB COM Port

print(device)