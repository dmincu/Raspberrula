# Raspberrula Game - Raspberry Hack


# Create enum type for all the different components on the
# raspberry pi
class Enum(set):
    def __getattr__(self, name):
        if name in self:
            return name
        raise AttributeError

devices = Enum(["CVBS", "GPIO", "JACK", "LED", "DSI", "CPUGPU", 	\
				"EthernetController", "USB", "USBPower", "HDMI", 	\
				"CSI", "EthernetRJ45"])

# Define functions associated with component 
def cvbs():
	print 1

def gpio():
	print 2

def jack():
	print 3

def led():
	print 4

def dsi():
	print 5

def cgpu():
	print 6

def ethcnt():
	print 7

def usb():
	print 8

def usbpow():
	print 9

def hdmi():
	print 10

def csi():
	print 11

def ethrj45():
	print 12

# Dictionary used to select function by component name
functions = {
	devices.CVBS: cvbs,
	devices.GPIO: gpio,
	devices.JACK: jack,
	devices.LED: led,
	devices.DSI: dsi,
	devices.CPUGPU: cgpu,
	devices.EthernetController: ethcnt,
	devices.USB: usb,
	devices.USBPower: usbpow,
	devices.HDMI: hdmi,
	devices.CSI: csi,
	devices.EthernetRJ45: ethrj45
}

# Class used to instantiate component with method to print
# information
class DeviceInfo:
	def __init__(self, devname):
		self.devname = devname

	def printInfo(self):
		func = functions[self.devname]
		func()

#TODO: remove - just for testing purposes
mydev = DeviceInfo("USB")
mydev.printInfo()
