# Raspberrula Game - Raspberry Hack

import sys

devdict = {}
limdict = {}
portaldict = {}

# Parser functions for device info and collision detection
def parse_file():
	f = open('../others/Info.txt', 'r')
	data = f.read()
	splat = data.split("\n\n")
	splat2 = len(splat) * [[]]
	for i in range(len(splat) - 1):
		splat2[i] = splat[i].split(":\n\t")
		devdict[splat2[i][0]] = splat2[i][1]

def parse_limits():
	f = open('../others/map limits', 'r')
	data = f.read()
	splat = data.split("\n\n")
	splat2 = len(splat) * [[]]
	for i in range(len(splat) - 1):
		splat2[i] = splat[i].split(":\n\t")
		limdict[splat2[i][0]] = splat2[i][1].split("\n\t")

def parse_portal():
	f = open('../others/portale', 'r')
	data = f.read()
	splat = data.split("\n\n")
	splat2 = len(splat) * [[]]
	for i in range(len(splat) - 1):
		splat2[i] = splat[i].split(":\n\t")
		portaldict[splat2[i][0]] = splat2[i][1]

# Class used to instantiate component with method to get
# information
class Devices:
	def __init__(self):
		self.my_list = []
		parse_file()
		parse_limits()
		parse_portal()

	def add_device(self, devname):
		self.my_list.append(DeviceInfo(devname))

	def add_all_devices(self):
		self.my_list = []
		for key, value in devdict.iteritems():
			self.my_list.append(DeviceInfo(key))

class DeviceInfo:
	def __init__(self, devname):
		self.devname = devname
		self.limits = limdict[self.devname]
		self.info = devdict[self.devname]
		self.portal = portaldict[self.devname]

	def get_name(self):
		return self.devname

	def get_info(self):
		return self.info + "\n"

	def get_limits(self):
		return self.limits

	def get_portal_coord(self):
		aux = self.portal.split(" ")
		return [int(aux[0]), int(aux[1])]

	def get_upper(self):
		aux = self.limits[0].split(" ")
		return [int(aux[0]), int(aux[1])]
	
	def get_lower(self):
		aux = self.limits[len(self.limits) - 1].split(" ")
		return [int(aux[0]), int(aux[1])]
