# Titouan Teyssier 19/02/2017
import sys
from twilio.rest import TwilioRestClient

"""
fill those four variables with your informations
(you have to make a twilio account)
"""

accountSID = 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
authToken = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
myTwilioNumber = '+33122334455'
myCellPhone = '+33118218072'

def send(msg):
	client = TwilioRestClient(accountSID, authToken)
	client.messages.create(
		to = myCellPhone,
		from_ = myTwilioNumber,
		body = msg
	)
