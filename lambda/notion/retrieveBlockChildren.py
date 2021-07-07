import requests
import os
import sys
sys.path.append("./")
import constants

def retrieveBlockChildren(blockId, accessToken):
	url = constants.NOTION_RETRIEVE_BLOCK_CHILDREN_URL
	url = url.replace("<blockId>", blockId)

	customHeader={
		"Authorization" : "Bearer " + accessToken,
		"Content-Type":"application/json",
		"Notion-Version" : constants.NOTION_VERSION
	}
	response = requests.get(url, headers=customHeader)
	return response.json()