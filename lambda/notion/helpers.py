import logging
from typing import List
import os
import sys
sys.path.append("./")
import constants
from notion import search
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)



def isTypeWorkspace(page):
    if(page.get("parent") and page.get("parent").get("type") == "workspace"):
        return True
    else:
        return False

def isType(block,type):
    if(block.get("type") == constants.TYPE[type]):
        return True
    else:
        return False

def getPlainText(block):
    try:
        return block.get(block.get("type")).get("text").get("plain_text")
    except:
        return "text not found!"


def getPageName(page):
    try:
        if(page.get("object") == "page"):
            return page.get("properties").get("title").get("title")[0].get("text").get("content")
        if(page.get("object") == "database"):
            return page.get("title")[0].get("text").get("content")
    except :
        logger.error("Page not available")

def getDataFromBlockBasedType(type,blocks):
    logger.info(blocks)
    try:
        typeObjects = list(map(getPlainText, filter(lambda block: isType(block,type), blocks)))
        return typeObjects
    except:
        logger.error("block not found")
        return list("Data could not be extracted")

def getPageIdfromPageName(pageName, accessToken):
    try:
        response = search(pageName, accessToken)
        # Assumption: there exists only 1 page with a name

        if(len(response.get("results"))):
            return "Page not found"
        page = response.get("results")[0]
        return page.get("id")
    except: 
        logger.error("Page not available")
        return "Page not found"
