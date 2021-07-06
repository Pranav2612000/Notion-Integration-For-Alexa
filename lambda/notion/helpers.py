import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

def isTypeWorkspace(page):
    if(page.get("parent") and page.get("parent").get("type") == "workspace"):
        return True
    else:
        return False

def getPageName(page):
    try:
        if(page.get("object") == "page"):
            return page.get("properties").get("title").get("title")[0].get("text").get("content")
        if(page.get("object") == "database"):
            return page.get("title")[0].get("text").get("content")
    except :
        logger.error("Page not available")
