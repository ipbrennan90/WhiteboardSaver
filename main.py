from gpiozero import LED
import time
import logging
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
logging.debug("test")
led = LED(17)

def main():
    logging.debug("sleeping")
    time.sleep(6)
    logging.debug("turning led on")
    led.on()
    return

main()
    
