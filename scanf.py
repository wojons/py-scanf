import re

class Scanf(object):
	def __init__(self, f=""):
		
		self.matches = {'%s' : "(\S+)", '%d' : '(\d+)'}
		
		if f != "":
			self.make(f)
	
	def make(self, f):
		#print self.matches
		#for dex, dat in self.matches:
			#f = f.replace(dex, dat)
		f = f.replace('%s', "(\S+)")
		f = f.replace('%d', "(\d+)")
		self.re = re.compile(f)
		
	def sscanf(self, s):
		reg = self.re.split(s)
		return reg[1:-1]

#scan = Scanf()
#scan.make('%s - %d %s, %d %s')
#print scan.sscanf('/usr/sbin/sendmail - 0 errors, 4 warnings')
