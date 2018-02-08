from gpiozero import LED
import time
import logging
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
logging.debug("test")
led = LED(17)

def main():
    while True:
        led.on()
        logging.debug("on")
        time.sleep(10)
        led.off()
        logging.debug("off")
        time.sleep(10)
    

main()
    
