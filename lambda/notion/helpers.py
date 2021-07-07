import logging
import search
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