import hashlib
import json
from time import time
chain=[]
def block(proof,previous_hash=  None):
	transaction = {
		"sender":"Satoshi",
		"receiver":"Mike",
		"amount":"5 ETH"
	}
	data = {
		"block height":"1",
		"block reward":"2.046327048499942521 ETH (2 + 0.046327048499942521)",
		"timestamp":time(),
		"transaction":transaction,
		"gas/fee":0.1,
		"gas limit":"14,999,907",
		"proof":proof,
		"previous_hash":previous_hash
	}
	chain.append(data)
	print("Block information: ",data)
	string_object = json.dumps(data)
	block_string = string_object.encode()
	raw_hash = hashlib.sha256(block_string)
	hex_hash = raw_hash.hexdigest()
	print("hashcode of block : ",hex_hash)
block(previous_hash = "no previous hash.Since this is the first block.",proof = 000)