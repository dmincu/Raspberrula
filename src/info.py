# Raspberrula Game - Raspberry Hack

import sys

dict = {}

def parse_file():
	f = open('../others/Info.txt', 'r')
	data = f.read()
	splat = data.split("\n\n");
	splat2 = len(splat) * [[]]
	for i in range(len(splat) - 1):
		splat2[i] = splat[i].split(":\n\t");
		dict[splat2[i][0]] = splat2[i][1]

# Class used to instantiate component with method to print
# information
class DeviceInfo:
	def __init__(self, devname):
		self.devname = devname

	def getInfo(self):
		return dict[self.devname] + "\n"

#TODO: remove - just for testing purposes
parse_file()
mydev = DeviceInfo("CVBS")
sys.stdout.write(mydev.getInfo())
