#For parsing the XML file, we will be using the BeautifulSoup module along with html parser. First, we need to install the latest BeautifulSoup4 package using the following command.
#pip3 install lxml

from typing import Optional

from lxml import etree as et


def readxml(filename, path, variable, index = 1):

# index = 0 means all tag in the list
# index= 1 to {count of tags} means the item line to read in the list
# index > {count of tags} is ignored

    tree = et.parse(filename)
    tags = tree.xpath(path + "/" + variable)
    cnt = len(tags)

    if cnt != 0 and cnt >= index and index >= 0:
        if index == 0:
            ret = ""
            for tag in tags:
                ret = ret + tag.text + ";"
            return ret
        else:
            return tags[index-1].text
    else:
        return ""



def writexml(filename, path, variable, value, index = 1):

#index = 0 means all tag in the list
#index = -1 means a new tag in the list
#index= 1 to {count of tags} means the item line to modify in the list
#index > {count of tags} is ignored

    tree = et.parse(filename)
    root = tree.getroot()
    tags = tree.xpath(path+"/"+variable)

    found = False
    if len(tags) == 0 or index == -1:
        parent = tree.xpath(path)
        if len(parent) > 0:
            selt = et.SubElement(parent[0], variable)
            selt.text = value
            found = True
    #elif len(tags) != 0 and len(tags) >= index:
    elif len(tags) >= index:
        found = True
        if index == 0:
            for tag in tags:
                tag.text = value
        else:
            tags[index-1].text = value

    indent_xml(root)
    #result = et.tostring(root, encoding="unicode")
    #print(result)

    et.ElementTree(root).write(filename, encoding='UTF-8', pretty_print=True, xml_declaration=True)


def indent_xml(element: et.Element, level: int = 0, is_last_child: bool = True) -> None:
    space = "    "
    indent_str = "\n" + level * space

    element.text = strip_or_null(element.text)
    num_children = len(element)

    #if element.text:
    #    element.text = f"{indent_str}{space}{element.text}"

    if num_children:
        element.text = f"{element.text or ''}{indent_str}{space}"

        for index, child in enumerate(element.iterchildren()):
            is_last = index == num_children - 1
            indent_xml(child, level + 1, is_last)

    elif element.text:
        element.text = f"{element.text}"
        #element.text += indent_str

    tail_level = max(0, level - 1) if is_last_child else level
    tail_indent = "\n" + tail_level * space
    tail = strip_or_null(element.tail)
    element.tail = f"{indent_str}{tail}{tail_indent}" if tail else tail_indent


def strip_or_null(text: Optional[str]) -> Optional[str]:
    if text is not None:
        return text.strip() or None
