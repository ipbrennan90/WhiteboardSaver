from gpiozero import LED
import time
import logging
from twilio.rest import Client
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
logging.debug("test")
led = LED(17)
account_sid = os.environ['TWILIO_ACCT']
auth_token = os.environ['TWILIO_TOKEN']
twilio_client = Client(account_sid, auth_token)


def message():
    try:
        body = twilio_client.messages.create(
            "+13033190247",
            body="I turned on!",
            from_="+17205482762",
            status_callback="https://requestb.in/12hql6p1"
        )
    except IOError as e:
        print 'ERROR: {}'.format(e)
    finally:
        print("DID IT")
        
def main():
    logging.debug("start")
    led.off()
    time.sleep(10)
    led.on()
    logging.debug("on")
    time.sleep(10)
    

main()
    
