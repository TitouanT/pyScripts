#!/usr/bin/python3

# Titouan Teyssier 19/02/2017
from edt import Edt, extractTime
from datetime import date, datetime
import sys

def display(day):
	print (day[0].day() + '\n\t' + str(day).replace('\n', '\n\t'))

def interpreter(edt):
	arg = sys.argv

	length = len(arg) - 1
	if (length == 0):
		name = sys.argv[0].replace('./', '')
		print (
			'USAGE: {} <all | week "index of week"'
			' | from "d1" to "d2" | to "day" | '
			'"liste of days">'.format(name)
		)
		print('Exemple:')
		print('\t{} all          # display all the entries'.format(name))
		print('\t{} week 0       # display the timetable for the week'.format(name))
		print('\t{} from 1 to 4  # display the timetable from tomorrow to 4 (included)'.format(name))
		print('\t{} to 3         # display the timetable for 4 days'.format(name))
		print('\t{} 2            # display the timetable in 2 days'.format(name))
		exit()

	days = []
	if arg[1] == 'week':
		tD = extractTime(datetime.now().strftime("%Y%m%dT%H%M%SZ"))
		fD = extractTime(edt[0]['DTSTART'])
		delta = (date(tD['year'], tD['month'], tD['day']) - date(fD['year'], fD['month'], fD['day'])).days
		for week in arg[2:]:
			first = delta + int(week) * 7
			days += range(first, first + 7)

	elif arg[1] == 'all':
		days = range(-7, edt.nbWeek * 7)

	elif arg[1] == 'from' or arg[1] == 'to':
		begin = 0 if arg[1] == 'to' else int(arg[2])
		end = int(arg[-1])
		if begin < end:
			end += 1
			step = 1
		else:
			end -= 1
			step = -1
		days = range(begin, end, step)

	else:
		days = [int(j) for j in sys.argv[1:]]

	return days

edt = Edt()
edt.createEdt()

days = interpreter(edt)

print('----------------- start of message -----------------')
for j in days:
	edt1day = edt.day(j)
	if (len(edt1day) > 0):
		display(edt1day)
print('T2')
print('------------------ end of message ------------------')