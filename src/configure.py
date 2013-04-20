# Raspberrula Game - Raspberry Hack

import easygui

class DeviceConfigure:

	def __init__(self, devices):
		self.devices = devices

	def popup(self, device):
		easygui.msgbox(device.get_info(), title = device.get_name())		
