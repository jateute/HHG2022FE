import os
import serial
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
        device: str = port
    # OpenMV Cam USB COM Port

if len(device) <= 0: raise RuntimeError('Couldn\'t find the openmv cam')
conn = serial.Serial(device)
conn.write(b'start')
print('Started connection with OpenMV Cam')
try:
    while True:
        print(conn.read_all().decode('UTF-8'), end="")
finally:
    print("Closing connection")
    if not conn.closed: conn.close()