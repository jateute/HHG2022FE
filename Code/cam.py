import sensor, pyb
import json, time

THRESHOLDS = [
    (32, 42, 49, 62, 27, 50), # Red pillars
    (42, 56, -47, -27, 10, 35)# Green pillars
] # Constants for color tracking

sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)

# Flip the image because the camera is upside down
sensor.set_vflip(True)
sensor.set_hmirror(True)

sensor.set_auto_gain(False) # Need to turn this off for colour tracking
sensor.set_auto_whitebal(False) # Also turn this off for colour tracking
sensor.set_brightness(+3) # Turn brightness up for clearer colors

sensor.skip_frames(time=2000)

led = pyb.LED(3)
usb = pyb.USB_VCP()
usb.init()

def main():
    img = sensor.snapshot()
    usb.send('BEGIN\n'.encode('UTF-8')) # Start of new Data
    for blob in img.find_blobs(THRESHOLDS, pixels_threshold=10, area_threshold=10, merge=True):
        data = {
            'type': blob.code(),
            'rect': blob.rect(),
            'size': blob.size()
        }
        usb.send(f'{json.dumps(data)}\n'.encode('UTF-8'))
        img.draw_rectangle(blob.rect())
        pass

    usb.send('END\n'.encode('UTF-8')) # End of now Data
    pass

while True:
    while (usb.isconnected()==False): time.sleep_ms(100)
    main()
    pass
