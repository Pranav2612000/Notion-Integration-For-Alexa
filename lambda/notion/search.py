import requests
import os
import sys
sys.path.append("./")
import constants

def search(query,accessToken):
	data={
		"query":query,
		"sort":{
			"direction":"ascending",
			"timestamp":"last_edited_time"
		}
	}
	customHeader={
		"Authorization" : "Bearer " + accessToken,
		"Content-Type":"application/json",
		"Notion-Version" : constants.NOTION_VERSION
	}
	url=constants.NOTION_SEARCH_URL
	response=requests.post(url,headers=customHeader,json=data)
	return response.json()

