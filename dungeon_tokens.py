import urllib2
import dungeon_tokens_func
import sys

try:
	api_key = sys.argv[1]
	try:
		print(dungeon_tokens_func.get_tokens(api_key))
	except urllib2.HTTPError, e:
		print("No valid API key found")
	except urllib2.URLError, e:
		print("Check your internet connection")
except IndexError:
	print("API key missing as argument")
