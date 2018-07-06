#!/usr/bin/env python3
# -*- coding: utf-8 -*- 
import os
import sys
import subprocess

try: gelen_parametre = sys.argv[1]
except: gelen_parametre = ""

def basla():
	if gelen_parametre == "gizle": 
		gizle()
	elif gelen_parametre == "goster": 
		goster()
	else:
		xfce_panel_kontrolu = subprocess.check_output("xfce4-panel")	
		if "already" in str(xfce_panel_kontrolu): gizle()
		else: goster()

def gizle():
	print("gizle")
	os.system("killall xfce4-panel")
	#os.system('xmodmap -e "pointer = 1 2 99"')#mouse sağ click gizle
	
def goster():
	print("goster")
	os.system("xfce4-panel")
	#os.system('xmodmap -e "pointer = 1 2 32 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 3"')#mouse sağ click goster
				
if __name__ == '__main__':	
	basla()
	
	
