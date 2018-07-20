#!/usr/bin/env python3
# -*- coding: utf-8 -*- 
import os
import json

basladigim_yer = "/root/cpuhunter"
config_dosyasi = basladigim_yer + "/config.json"

def basla():
	jsonFile = open(config_dosyasi, "r") # Open the JSON file for reading
	config = json.load(jsonFile) # Read the JSON into the buffer
	jsonFile.close() # Close the JSON file

	auto_reboot = config["config"]["auto_reboot"] 

	if auto_reboot == "True": 
		config["config"]["auto_reboot"] = "False"
		jsonFile = open(config_dosyasi, "w+")
		jsonFile.write(json.dumps(config, indent=4, sort_keys=True))
		jsonFile.close()
		alert("auto_reboot disabled")
	else:
		alert("auto_reboot disabled already")

def alert(message):
	print(message)
	os.system("notify-send " + "'" + message + "'")
	
if __name__ == "__main__":
	basla()
