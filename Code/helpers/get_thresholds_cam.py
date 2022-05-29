import sensor, pyb, image # Imports for the camera
import time

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

usb = pyb.USB_VCP()
usb.init()

l:list[int] = []
a:list[int] = []
b:list[int] = []

def get_value(v:list[int]) -> tuple:
    avg = sum(v)/len(v)
    min_v = avg - 10
    max_v = avg + 10
    if min_v > min(v): min_v = min(v)
    if max_v < max(v): max_v = max(v)
    return int(min_v), int(max_v)

while True:
    if not usb.isconnected():
        time.sleep_ms(100)

    else:
        for i in range(1, 1000):
            img = sensor.snapshot()
            lv, av, bv = image.rgb_to_lab(img.get_pixel(160,120))
            img.draw_cross(160,120)

            l.append(int(lv))
            a.append(int(av))
            b.append(int(bv))
        min_l, max_l = get_value(l)
        min_a, max_a = get_value(a)
        min_b, max_b = get_value(b)
        threashold = (min_l, max_l, min_a, max_a, min_b, max_b)
        usb.send(str(threashold).encode('UTF-8'))
        break
