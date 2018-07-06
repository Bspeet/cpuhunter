#!/usr/bin/env python3
# -*- coding: utf-8 -*- 
import os
import json

basladigim_yer = "/root/cpuhunter"
ayarlar_dosyasi = basladigim_yer + "/ayarlar.json"

def basla():
	jsonFile = open(ayarlar_dosyasi, "r") # Open the JSON file for reading
	ayarlar = json.load(jsonFile) # Read the JSON into the buffer
	jsonFile.close() # Close the JSON file

	auto_reboot = ayarlar["ayarlar"]["auto_reboot"] 

	if auto_reboot == "True": 
		ayarlar["ayarlar"]["auto_reboot"] = "False"
		jsonFile = open(ayarlar_dosyasi, "w+")
		jsonFile.write(json.dumps(ayarlar, indent=4, sort_keys=True))
		jsonFile.close()
		alert("auto_reboot disabled")
	else:
		alert("auto_reboot disabled already")

def alert(message):
	print(message)
	os.system("notify-send " + "'" + message + "'")
	
if __name__ == "__main__":
	basla()
