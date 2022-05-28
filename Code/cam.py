import sensor, pyb
import json, time

THRESHOLDS = [
    (35,43,53,65,33,40), # Red pillars (code: 1)
    (14,18,-4,-3,0,1),# Green pillars (code: 2)
    (10,-10,0, 20,0,7) # Black walls (code: 4)
]
"""Holds the threshold values for colour tracking"""

sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.skip_frames(time=2000)
sensor.set_auto_gain(False) # Need to turn this off for colour tracking
sensor.set_auto_whitebal(False) # Also turn this off for colour tracking
# Flip the image as the camera is upside down
sensor.set_vflip(True)
sensor.set_hmirror(True)

led = pyb.LED(3)
usb = pyb.USB_VCP()
usb.init()

def main():
    img = sensor.snapshot()
    usb.send('BEGIN\n'.encode('utf-8')) # Start of new Data
    for blob in img.find_blobs(THRESHOLDS, pixels_threshold=10, area_threshold=10, merge=True):
        data = {
            'type': blob,
            'rect': blob.rect()
        }
        usb.send(f'{json.dumps(data)}\n'.encode('utf-8'))
        pass

    usb.send('END\n'.encode('utf-8')) # End of now Data
    pass

while True:
    while (usb.isconnected()==False): time.sleep_ms(100)
    main()
    pass