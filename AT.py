from gpiozero import DistanceSensor
from gpiozero import LED
from picamera import PiCamera
from time import sleep

def project():
    c = PiCamera()
    led = LED(4)
    i = 0
    #In theory we could loop this with some condition, however the condition I had planned didn't work
    while i < 1:
        c.start_recording('/home/Documents/video/video' + str(i) + '.h264')
        led.on()
        sleep(5)
        camera.stop_recording()
        led.off()
        sleep(5) #We wait 5 seconds
main():
    project()

main()

