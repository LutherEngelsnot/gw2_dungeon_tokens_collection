from urllib.request import HTTPError,URLError
import dungeon_tokens_func_3
from sys import argv

try:
	api_key = argv[1]
	try:
		print(dungeon_tokens_func_3.get_tokens(api_key))
	except HTTPError:
		print("No valid API key found")
	except URLError:
		print("Check your internet connection")
except IndexError:
	print("API key missing as argument")
