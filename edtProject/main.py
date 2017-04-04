#!/usr/bin/python3

# Titouan Teyssier 19/02/2017
from edt import Edt, extractTime
import sms
import datetime
from time import sleep
from seconds import Sec

firstTurn = True
sendTime = Sec(18,0,0)

while True:
	edt = Edt()
	edt.createEdt()

	currentTime = datetime.datetime.now().strftime("%Y%m%dT%H%M%SZ")
	currentSec = Sec.fromDict(extractTime(currentTime, timezone=0))
	sec = currentSec.to(sendTime)

	if (firstTurn and sec.sec > Sec(h=12).sec) or not firstTurn:
		edt1day = edt.today()
#		edt1day = edt.tomorrow()
		if len(edt1day)>0:
			print('----------------- begin of message -----------------')
			print(edt1day[0].day() + '\n' + str(edt1day) + '\nT2')
			sms.send('_\n' + edt1day[0].day() + '\n' + str(edt1day) + '\nT2')
			print('------------------ end of message ------------------')
	firstTurn = False

	print (
		'Entering sleep mode for {delta} from {now} to {final}'.format (
			delta = sec,
			now = currentSec,
			final = sendTime
		)
	)
	sleep(sec.sec)
	print('Sleep mode over !!')
