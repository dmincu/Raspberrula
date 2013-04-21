# Raspberrula Game - Raspberry Hack

import easygui
import subprocess
import paramiko

class DeviceConfigure:

	def __init__(self, devices):
		self.devices = devices
		
	def ethcontr(self):
		# Set parameters for input box
		msg = "Enter details for connection to another computer"
		title = "Ethernet Controller"
		fieldNames = ["Computer IP", "User"]
		fieldValues = []
		fieldValues = easygui.multenterbox(msg, title, fieldNames)
		if fieldValues == None:
			return
		reply = easygui.passwordbox("Enter password")
		if reply == None:
			return	
	
		# Connect through SSH
		ssh = paramiko.SSHClient()
		ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		
		if (fieldValues[0] == "" or fieldValues[1] == ""):
			return
		
		ssh.connect(fieldValues[0], username=fieldValues[1], password=reply)
		
		while True:
			# Set parameters for query
			msg2 = "Enter command to run"
			title2 = "Connected to " + fieldValues[1] + "@" + fieldValues[0]
			fieldNames2 = ["Command"]
			fieldValues2 = []
			fieldValues2 = easygui.multenterbox(msg2, title2, fieldNames2)
			
			if (fieldValues2 == None or fieldValues2[0] == ""):
				break
			
			if cmp(fieldValues2[0], 'exit') == 0:
				break

			stdin, stdout, stderr = ssh.exec_command(fieldValues2[0])
			
			# Compose output
			output = ""
			for line in stdout:
				output = output + "\n" + line
			if output != "":	
				easygui.codebox("Command result", "Show result", output)

	def popup(self, device):
		choices = ["Exit", "Others(Info/Config)"]
		reply = easygui.buttonbox(device.get_info(), title = device.get_name(), choices = choices)
		
		# Select between all types of components to see which window to draw
		if cmp(reply, 'Others(Info/Config)') == 0:
			if cmp(device.get_name(), 'EthernetRJ45') == 0:
				subprocess.call("./scripts/rj45.sh > buff", shell=True);
				f = open("buff","r");
				reply = easygui.msgbox(f.read(), title = "Ethernet Info")
				f.close()
			elif cmp(device.get_name(), 'CPUGPU') == 0:
				choices = ["CPU","GPU","SystemLoad"]
				reply = easygui.buttonbox("Choose..", choices=choices)
				if cmp(reply, 'CPU') == 0:
					subprocess.call("./scripts/cpu.sh > buff", shell=True);
					f = open("buff","r");
					reply = easygui.msgbox(f.read(), title = "CPU Info")
					f.close()
				elif cmp(reply, 'GPU') == 0:
					subprocess.call("./scripts/gpu.sh > buff", shell=True);
					f = open("buff","r");
					reply = easygui.msgbox(f.read(), title = "GPU Info")
					f.close()
				else:
					subprocess.call("./scripts/sysload.sh > buff", shell=True);
					f = open("buff","r");
					reply = easygui.msgbox(f.read(), title = "System Load Info")
					f.close()
			elif cmp(device.get_name(), 'USB') == 0:
				subprocess.call("./scripts/usb.sh > buff", shell=True);
				f = open("buff","r");
				reply = easygui.msgbox(f.read(), title = "USB Info")
				f.close()
			elif cmp(device.get_name(), 'USBPower') == 0:
				reply = easygui.msgbox("Power is On", title = "Power Info")
			elif cmp(device.get_name(), 'EthernetController') == 0:
				choices = ["Connect through SSH"]
				reply = easygui.buttonbox("Connection", choices=choices)
				self.ethcontr()
			else:
				reply = easygui.msgbox("No other info(Sorry:))", title = device.get_name(), ok_button = "Exit")
