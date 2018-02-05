from gpiozero import LED
import time
led = LED(17)

def main():
    time.sleep(6)
    led.on()

main()
    
