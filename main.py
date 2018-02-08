from gpiozero import LED
import time
import logging
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
logging.debug("test")
led = LED(17)

def main():
    logging.debug("start")
    led.off()
    time.sleep(10)
    led.on()
    logging.debug("on")
    time.sleep(10)
    

main()
    
