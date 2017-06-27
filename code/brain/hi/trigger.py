import json
from pprint import pprint
from random import randint

with open('brain/hi/hi_gif.json') as data_file:    
	    	data = json.load(data_file)

pprint(data)

def random():
	up = len(data)
	
	return (data[randint(0, up-1)]["link"])
