from gpiozero import LED
import time
import logging
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
logging.debug("test")
led = LED(17)

def main():
    led.off()
    

main()
    
