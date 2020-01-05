#!/bin/python

import sys
import requests
import xml.etree.ElementTree as ET

userName='user'
password='pass'

def update_lease(vCloud, org):
	loginUser=userName+'@'+org
	headers={'Accept':'application/*+xml;version=27.0'}

	#Disable Certificate checking
	requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)
	session = requests.Session()
	session.verify = False

	#Login to Cloud
	r=session.post('https://'+vCloud+'/api/sessions', auth=(loginUser,password), headers=headers)
	if (r.status_code != 200): r.raise_for_status()

	# Add authorization header
	headers['x-vcloud-authorization']=r.headers['x-vcloud-authorization']

	#Get List of vApp
	r=session.get('https://'+vCloud+'/api/vApps/query', headers=headers)
	if (r.status_code != 200): r.raise_for_status()

	#Parse XML and get URL for vApp
	vApps=[];
	doc=ET.fromstring(r.text);
	for vAppRec in doc.findall('*/[@vdc]'):
	   vApps.append(vAppRec)

	#Get the current leaseSettingsSection and put the same to get new lease
	for vAppRec in (vApps):
	   print(vAppRec.attrib['name'])
	   r=session.get(vAppRec.attrib['href']+'/leaseSettingsSection', headers=headers)
	   print(r.text)
	   if (r.status_code != 200): r.raise_for_status()

	   r=session.put(vAppRec.attrib['href']+'/leaseSettingsSection', headers=headers, data=r.text)
	   if (r.status_code != 200): r.raise_for_status();

update_lease('vAppUrl','vAppOrg')