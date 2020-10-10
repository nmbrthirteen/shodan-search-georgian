# -*- coding: utf-8 -*-
import shodan
import os
import time
import datetime

SHODAN_API_KEY = "PSKINdQe1GyxGgecYz2191H2JoS9qvgD"

api = shodan.Shodan(SHODAN_API_KEY)

def find_only_ip():
	try:
		results = api.search('''{s}'''.format(s=search))
		print('Shedegebi napovnia: %s' % results['total'])
		for result in results['matches']:
				print('{}'.format(result['ip_str']))
	except (shodan.APIError)as e:
		print('Errori: {}'.format(e))
def find():
	try:
		results = api.search('''{ts}'''.format(ts=search))
		print('Shedegebi napovnia: %s' % results['total'])
		for result in results['matches']:
				print('IP: {}'.format(result['ip_str']))
				print(result['data'])
				print('')
	except (shodan.APIError)as e:
		print('Errori: {}'.format(e))
		var = find()
print('''
 ____  _   _  ___  ____    _    _   _ _____ ____  _____ _____
/ ___|| | | |/ _ \|  _ \  / \  | \ | |  ___|  _ \| ____| ____|
\___ \| |_| | | | | | | |/ _ \ |  \| | |_  | |_) |  _| |  _|
 ___) |  _  | |_| | |_| / ___ \| |\  |  _| |  _ <| |___| |___
|____/|_| |_|\___/|____/_/   \_|_| \_|_|   |_| \_|_____|_____|
translated by Nmbrthirteen
''')
print('''Es aris ufaso sadziebo sistema Shodan ze.
gvaqvs filtrebi(magalitad):
country:qveyana
city:qalaqi
geo:geolokacia
hostname:hosti
net:ip misamarti
os:operaciuli sistema
port:porti

gamoiyenet Ctrl+C programis gasatishad''')



search = input('sheikvanet sadziebo sityva==>')

question = input('''Romeli gchirdebat? tu kvela monacemi, sheikvanet - all / tu mxolod ip, sheikvanet - ip==>''')

if question == ("ip"):
	find_only_ip()
elif question == ("all"):
	find()
else:
	print('Tqven arasworad sheikvanet monacemebi, programa gaitisha...')
