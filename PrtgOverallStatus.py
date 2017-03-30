# -*- coding: utf-8 -*-

import sys
import json
from paepy.ChannelDefinition import CustomSensorResult
import urllib.request

from xml.etree import ElementTree as ET

API_BASE_URL = "/api/gettreenodestats.xml"

def getInfos(params):

	try:
		#Parsing script's parameters
		inputs = params['params'].split()
		
		url_coreserver = inputs[0]
		username = inputs[1]
		passhash = inputs[2]

		if (("http" not in url_coreserver) and ("https" not in url_coreserver)):
			url_coreserver = "https://"+inputs[0]
	
		#Query 
		query = url_coreserver + API_BASE_URL + "?" + "username="+username+"&"+"passhash="+passhash
		res   = urllib.request.urlopen(query)

		root = ET.parse(res).getroot()
		success(root, url_coreserver)
		
	except:
		error("Could not load data: please check sensor's parameters.")

def success(root, url_coreserver):
	
	#Parsing the XML
	prtg_version = root.find("prtg-version").text
	servertime   = root.find("servertime").text
	totalsens    = root.find("totalsens").text 
		
	upsens    = root.find("upsens").text 
	downsens    = root.find("downsens").text 
	warnsens    = root.find("warnsens").text 
	downacksens    = root.find("downacksens").text 
	partialdownsens    = root.find("partialdownsens").text 
	unusualsens    = root.find("unusualsens").text 
	pausedsens    = root.find("pausedsens").text 
	undefinedsens    = root.find("undefinedsens").text 
	
	message = "Status of the PRTG " + prtg_version+" at "+url_coreserver
	
	printOut(message, upsens, downsens,warnsens,downacksens, partialdownsens, unusualsens, pausedsens, undefinedsens )
	
	
	

def printOut(message, upsens, downsens,warnsens,downacksens, partialdownsens, unusualsens, pausedsens, undefinedsens ): 
	# Building sensor's output (channels)
	result = CustomSensorResult(message)
	
	result.add_channel(channel_name= "Up ", unit="Count", value= checkValue(upsens))
	result.add_channel(channel_name= "Down ", unit="Count", value= checkValue(downsens))
	result.add_channel(channel_name= "Warning", unit="Count", value= checkValue(warnsens))
	result.add_channel(channel_name= "Down Ack", unit="Count", value=checkValue(downacksens))
	result.add_channel(channel_name= "Partial Down", unit="Count", value=checkValue(partialdownsens))
	result.add_channel(channel_name= "Unsual", unit="Count", value=checkValue(unusualsens))
	result.add_channel(channel_name= "Paused", unit="Count", value=checkValue(pausedsens))
	result.add_channel(channel_name= "Undefined", unit="Count", value=checkValue(undefinedsens))
	
	print(result.get_json_result())
	
	
def error(message):
	printOut(message, None, None,None,None, None, None, None, None)

def checkValue(arg): 
	if arg is None: 
		return 0
	else : 
		return arg
		
def main():
	# Interpret first command line parameter as json object
	params = json.loads(sys.argv[1])
	getInfos(params)
       

if __name__ == '__main__':
    main()
