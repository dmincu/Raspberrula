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

# Class used to instantiate component with method to get
# information
class Devices:
	def __init__(self):
		self.list = []
		parse_file()

	def add_device(self, devname):
		self.list.append(DeviceInfo(devname))

	def add_all_devices(self):
		self.list = []
		for key, value in dict.iteritems():
			self.list.append(DeviceInfo(key))

class DeviceInfo:
	def __init__(self, devname):
		self.devname = devname
		self.info = dict[self.devname]

	def get_name(self):
		return self.devname

	def get_info(self):
		return self.info + "\n"
