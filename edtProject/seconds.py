class Sec:
	def __init__(self, h=0, m=0, s=0):
		self.sec = s + 60 * (m + 60 * h)

	@classmethod
	def fromDict(self, t):
		return Sec(h=t['hour'], m=t['min'], s=t['sec'])

	def hms(self):
		s = self.sec
		h = s // 3600
		s %= 3600
		m = s // 60
		s = s % 60
		return h, m, s

	def to(self, s):
		s1, s2 = self.sec, s.sec
		s = s2 - s1 if s2 >= s1 else Sec(h=24).sec - s1 + s2
		return Sec(s=s)

	def __str__(self):
		h, m, s = self.hms()
		return '{:02d}:{:02d}:{:02d}'.format(h, m, s)