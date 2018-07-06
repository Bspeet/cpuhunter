#!/usr/bin/env python3
# -*- coding: utf-8 -*- 

import os, sys, notify2
notify2.init("")
basladigim_yer = os.path.dirname(os.path.realpath(sys.argv[0]))
os.chdir(basladigim_yer)
	
def main():
	if os.path.exists("so"): sys.path.append("so")
	elif os.path.exists("py"): sys.path.append("py")
	else: alert("module folder not found", 10000); exit()
	import k
	k.basla()
	
def alert(message, timeout=1000):
	print(message)
	n = notify2.Notification(message)
	n.timeout = timeout
	n.show()
	
if __name__ == "__main__":
	main()
	
