# Titouan Teyssier 19/02/2017
import sys
from urllib.request import urlopen
from os import path
import datetime
import calendar

def removeJunkLines(lines):
	first, last = 0, 1
	while lines[first] != 'BEGIN:VEVENT': first += 1
	while lines[-last] != 'END:VEVENT': last += 1
	lines = [line for line in lines[first:len(lines)-last+1] if line.count(':') > 0 and line.count(')') == 0]
	return lines

def coursExtractor(lines):
	elt = Cours()
	i = 1;
	while lines[i] != 'END:VEVENT':
		key, attr = lines[i].split(':')
		elt[key] = attr
		i += 1

	del elt['DTSTAMP']
	del elt['UID']
	del elt['CREATED']
	del elt['SEQUENCE']

	return elt, lines[i+1:]

def updateEdt(url):
	edt = open(Edt.edtDir, 'wb')
	edt.write(urlopen(url).read())
	edt.close()

def extractTime(date2extract, timezone=2):
	date = {}
	date['year'] = int(date2extract[:4])
	date['month'] = int(date2extract[4:6])
	date['day'] = int(date2extract[6:8])
	date['hour'] = int(date2extract[9:11]) + timezone
	date['min'] = int(date2extract[11:13])
	date['sec'] = int(date2extract[13:15])
	return date


class Cours(dict):
	def __str__(self):
		dateStart = extractTime(self['DTSTART'])
		dateEnd = extractTime(self['DTEND'])
		representation = "{hdeb:02d}:{mdeb:02d} - {hfin:02d}:{mfin:02d}: {name} en {loca}\n".format (
			name = self['SUMMARY'],
			hdeb = dateStart['hour'],
			mdeb = dateStart['min'],
			hfin = dateEnd['hour'],
			mfin = dateEnd['min'],
			loca = self['LOCATION'] or '<voir UMTICE>'
		)
		return representation

	def day(self):
		t = extractTime(self['DTSTART'])
		indexDay = calendar.weekday(t['year'], t['month'], t['day'])
		name = calendar.day_name[indexDay]
		return '{name: <9} {day:02d}/{month:02d}'.format (
			day = t['day'],
			month = t['month'],
			name = name
		)

class Edt(list):
	# in this part if you don't want to see my courses in your remainder
	# you have to change the url to point towards your calendar
	urlFirst  = 'http://edt.univ-lemans.fr/jsp/custom/modules/plannings/anonymous_cal.jsp?resources='
	urlSecond = '&projectId=2&calType=ical&nbWeeks='
	edtDir = path.join(path.dirname(__file__), 'edt.ics')
	def __init__(self, resources=5121, nbWeek=4):
		self.url = "{first}{resources}{second}{nbWeek}".format (
			first = Edt.urlFirst,
			resources = resources,
			second = Edt.urlSecond,
			nbWeek = nbWeek
		)
		self.nbWeek = nbWeek

	def __str__(self):
		disp = ""
		for cours in self:
			disp += str(cours)
		return disp

	def createEdt(self):

		updateEdt(self.url)
		lines = [line.split('(')[0] for line in open(Edt.edtDir, 'r').read().split('\n')]
		lines = removeJunkLines(lines)

		while lines != []:
			elt, lines = coursExtractor(lines)
			self.append(elt)

		self.sort(key = lambda cours: int(cours['DTSTART'].replace('T', '').replace('Z', '')))

	def display(self):
		for cours in self:
			for k,v in cours.items():
				print("{key}: {value}".format(key = k, value = v))
			print()

	def day(self, delta):
		tday = extractTime((datetime.datetime.now() + datetime.timedelta(days=delta)).strftime("%Y%m%dT%H%M%SZ"))
		edtDay = Edt()
		for cours in self:
			tcours = extractTime(cours['DTSTART'])
			if (tcours['month'] == tday['month']
				and tcours['day'] == tday['day']):
				edtDay.append(cours)
			if (tcours['month'] > tday['month']
				or (tcours['month'] == tday['month']
				and tcours['day'] > tday['day'])):
				break
		return edtDay

	def today(self):
		return self.day(0)

	def tomorrow(self):
		return self.day(1)
