# gw2_dungeon_tokens_collection
Short python2 script to utilize the gw2 API to get the number of dungeon tokens you need additionally to finish all dungeon skin collection, already taking in account the number of tokens in the wallet.
### Requirements
Python2 script uses the moduls sys, urllib2 and json
Python3 script uses the moduls sys, urlib.request and json
### Install
Just download dungeon_tokens_func.py and dungeon_tokens.py and store them in the same folder for the Python2 script.
Download dungeon_tokens_func_3.py and dungeon_tokens_3.py and store them in the same folder for the Python3 script.
### Use
Call the script dungeon_tokens.py (for Python2) or dungeon_tokens_3.py (for Python3) following a space and the API-key of your account. The API-key need access rights for the wallet and progression.
### Example
*Python2:*

python dungeon_tokens.py 64D99BFC-050B-CF4C-A19C-65B836E1DA9704385872-E0A4-4E9E-8A93-717D6B20B583

*Python3:*

python dungeon_tokens_3.py 64D99BFC-050B-CF4C-A19C-65B836E1DA9704385872-E0A4-4E9E-8A93-717D6B20B583
