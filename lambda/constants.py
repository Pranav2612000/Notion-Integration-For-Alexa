NOTION_VERSION="2021-05-13"

NOTION_SEARCH_URL="https://api.notion.com/v1/search"
NOTION_RETRIEVE_BLOCK_CHILDREN_URL="https://api.notion.com/v1/blocks/<blockId>/children"

TYPE = {
    "todo" : "to_do",
    "to-do" : "to_do",
    "to do" : "to_do",
    "paragraph" : "paragraph",
    "heading" : "heading_1",
    "subheading" : "heading_2",
    "bulleted list" : "bulleted_list_item",
    "numbered list" : "numbered_list_item",
    "toggle" : "toggle",
    "child page" : "child_page",
}