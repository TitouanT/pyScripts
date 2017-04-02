#!/usr/bin/python3

# Titouan Teyssier 17/03/2017
from os import path
import sys

dataDir = path.join(path.dirname(__file__), 'data.txt')

class Serie:
	n = 0

	def __init__(self, name, season, episode, current, data):
		self.name = name
		self.s = season
		self.e = episode
		self.data = data
		self.id = Serie.n
		self.current = current
		self.known = season > 0
		Serie.n += 1

	def __str__(self):
		if self.known:
			disp = '{id:>2} {name:<28}:{se:^25} {cur} {data}'.format(
				id = self.id,
				name = self.name,
				se = 'S{s:0>2} E{e:0>2}'.format(
					s = self.s,
					e = self.e
				),
				cur = '***' if self.current else '   ',
				data = self.data
			)
		else:
			disp = '{id:>2} {name:<28}:{w:^25} {data}'.format(
				id = self.id,
				name = self.name,
				data = self.data,
				w = 'unknown'
			)
		return disp

	def formatData(self):
		return '{}:{}:{}:{:d}:{}'.format(
			self.name,
			self.s,
			self.e,
			self.current,
			self.data
		)

def readData():
	dataFile = open(dataDir, 'r')
	lines = dataFile.read().split('\n')
	dataFile.close()

	series = []
	for line in lines:
		if line != '':
			name, season, episode, current, data = line.split(':')
			series.append (
				Serie(name, int(season), int(episode), int(current), data)
			)

	return series

def writeData (series):
	dataFile = open(dataDir, 'w')
	string = ''
	for serie in series:
		string += serie.formatData() + '\n'
	dataFile.write(string)
	dataFile.close()

argv = sys.argv[1:]
argc = len(argv)

series = readData()

if argc == 0:
	for serie in series:
		print(serie)
	exit()

elif argv[0] == 'new' or argv[0] == 'n':
	serie = Serie(argv[1], int(argv[2]), int(argv[3]), 0, '')
	series.append(serie)
	series.sort(key = lambda serie: serie.name.replace(' ', '').lower())

elif argv[0] == 'up' or argv[0] == '+':
	index = int(argv[1])
	if argc > 2 and (argv[2] == 's' or argv[2] == 'S'):
		series[index].s += 1
		series[index].e = 1
	else:
		series[index].e += 1

elif argv[0] == 'set' or argv[0] == 's':
	index = int(argv[1])
	series[index].s = argv[2]
	series[index].e = argv[3]

elif argv[0] == 'known' or argv[0] == 'k':
	for serie in series:
		if serie.known:
			print(serie)
	exit()

elif argv[0] == 'unknown' or argv[0] == 'uk':
	for serie in series:
		if not serie.known:
			print(serie)
	exit()

elif argv[0] == 'current' or argv[0] == 'c':
	for serie in series:
		if serie.current:
			print(serie)
	exit()

elif argv[0] == 'toggle' or argv[0] == 't':
	index = int(argv[1])
	cur = series[index].current
	series[index].current = not cur

elif argv[0] == 'del' or argv[0] == '-':
	index = int(argv[1])
	del(series[index])

elif argv[0] == 'data' or argv[0] == 'd':
	index = int(argv[1])
	series[index].data = argv[2].replace(':', '')

else:
	print('usage: without argument to display the data')
	print('or with:')
	print('   new <name>  <season> <episode>                -> add a new serie')
	print('   up  <index> [\'S\' or \'s\' if up one season] -> augment by one episode of the serie at index')
	print('   set <index> <season> <episode>                -> set the last episode for the serie at index')
	print('   known                                         -> to display the series with a known last episode')
	print('   unknown                                       -> to display the other')
	print('   current                                       -> to display the series you are currently watching')
	print('   toggle <index>                                -> toggle the value of the current status of the serie at index')
	exit()

writeData(series)
