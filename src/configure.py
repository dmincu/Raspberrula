# Raspberrula Game - Raspberry Hack

import easygui

class DeviceConfigure:

	def __init__(self, devices):
		self.devices = devices

	def popup(self, device):
		choices = ["Exit", "Configure"]
		reply = easygui.buttonbox(device.get_info(), title = device.get_name(), choices = choices)
		if cmp(reply, 'Configure') == 0:
			reply = easygui.msgbox("Do Stuff", title = device.get_name(), ok_button = "Exit")