#!/usr/bin/env python
# -*- coding: utf-8 -*-

##########################
#                        #
#Emre Yılmaz (delosemre) #
# 	   emreylmz.com      #
# 	  kernelblog.org     #
##########################


from urllib.request import urlopen
import sys
import signal


def sigint_handler(signum, frame):
    print ("\n CTRL+C detected!")
    print(" \033[1;91m@Good bye\033[1;m")
    sys.exit() 
 
signal.signal(signal.SIGINT, sigint_handler)



def menu():
	print ("""\033[1;91m



                        (                                         
  (         (           )\ )       (          (                )  
  )\ )   (  )\         (()/(       )\ )       )\ )      (   ( /(  
 (()/(  ))\((_) (   (   /(_)) (   (()/(   (  (()/(     ))\  )\()) 
  ((_))/((_)_   )\  )\ (_))   )\ ) /(_))  )\  /(_))_  /((_)(_))/  
  _| |(_)) | | ((_)((_)|_ _| _(_/((_) _| ((_)(_)) __|(_))  | |_   
/ _` |/ -_)| |/ _ \(_-< | | | ' \))|  _|/ _ \  | (_ |/ -_) |  _|  
\__,_|\___||_|\___//__/|___||_||_| |_|  \___/   \___|\___|  \__|V1  

    
    1-) Find DNS Host Records (Subdomains)
    2-) Reverse DNS
    3-) DNS Lookup
    4-) Find Shared DNS Servers
    5-) Zone Transfer
    6-) Exit

                                                                  

                                 

\033[1;m""")

def geri():
	print("\n \033[1;91m1-) Return to main menu \n 2-) Exit \033[1;m")
	secimbir = input("root""\033[1;91m@emreylmz.com:~$\033[1;m ")
	if secimbir == "1":
		baslangic()
	if secimbir == "2":
		print(" \033[1;91m@GoodBye\033[1;m")
		sys.exit() 
	else:
		print(" Please enter one of the options in the menu. \n You return to the main menu!")
		baslangic()



def baslangic():
	menu()
	secim = input("    " + "delosemre" + "" "\033[1;91m@delosemre:~$\033[1;m ")

	if secim == "1":
		url = input("	Domain Name or IP Address: ")
		dnsl = ("https://api.hackertarget.com/hostsearch/?q=" + url)
		pdnsl = urlopen(dnsl).read()
		print (pdnsl)
		geri()
		
	if secim == "2":
		url = input("	DNS (8.8.8.8): ")
		dns = ("https://api.hackertarget.com/reversedns/?q=" + url)
		pdns = urlopen(dns).read()
		print (pdns)
		geri()
		

	if secim == "3":
		url = input("	Domain: ")
		host = ("https://api.hackertarget.com/dnslookup/?q=" + url)
		phost = urlopen(host).read()
		print (phost)
		geri()
		

	if secim == "4":
		url = input("	DNS Name (ns1.dnsserver.com): ")
		dnsa = ("https://api.hackertarget.com/findshareddns/?q=" + url)
		pdnsa = urlopen(dnsa).read()
		print (pdnsa)
		geri()
		

	if secim == "5":
		url = input("	Domain: ")
		zone = ("https://api.hackertarget.com/zonetransfer/?q=" + url)
		pzone = urlopen(zone).read()
		print (pzone)
		geri()
		

	if secim == "6":
		print ("GoodBye")
		quit()
	


baslangic()