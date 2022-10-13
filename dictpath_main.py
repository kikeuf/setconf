import re

from dictpath_utils import handle_search_dict_exceptions


def search_dict(dictDocument, pathItems: list):
    '''
    Uses parsed JSONPath components to recursively search though
    Python lists and dicts which represent a valid JSON structure.
    '''
    if len(pathItems) == 0:
        return dictDocument
    pathInfo = re.findall(r"[\w\s\d\-\+\%\']+", pathItems[0])

    # Searching a dict
    if len(pathInfo) == 1:  # searching a dict
        dictDocument = dictDocument.get(pathInfo[0])

    # Searching a list and we have the index
    elif len(pathInfo) == 2:
        field, index = pathInfo
        try:
            dictDocument = dictDocument.get(field)[int(index)]
        except IndexError:
            # This index does not exist in the data so we return nothing
            return None

    # Searching a list and we have a number of subfield/value pairs like [?subfield="value"]
    elif len(pathInfo) >= 3:
        field = pathInfo[0]
        if not isinstance(dictDocument.get(field), list):
            raise Exception(f'Cannot query {dictDocument.get(field)}. It is not a list')
        # Check for matches for each subfield/value pair
        countOfPairs = len(pathInfo) - 1
        for item in dictDocument.get(field):
            foundMatch = True
            pairsIndex = 1
            while pairsIndex < countOfPairs:
                subfield = pathInfo[pairsIndex]
                value = pathInfo[pairsIndex + 1].lstrip("'").rstrip("'")
                if str(item.get(subfield)) != value:
                    foundMatch = False
                    break
                pairsIndex += 2
            if foundMatch == True:
                dictDocument = item
                return search_dict(dictDocument, pathItems[1:])
                # If data being searched for couldn't be found, return None
        return None
    return search_dict(dictDocument, pathItems[1:])


def get_dict_item(dictDocument, path: str):
    '''
    Uses supplied JSONPath to search for and return a value or
    object from the JSON document.
    '''
    try:
        pathItems = path.split(".")[1:]
        result = search_dict(dictDocument, pathItems)
    except Exception as e:
        raise handle_search_dict_exceptions(path, e, 'Get item')
    return result


def update_dict_element(dictDocument, path: str, value):
    '''
    Upserts the value of the field specified by the supplied path.
    '''
    pathItems = path.split(".")[1:]
    try:
        containingDict = search_dict(dictDocument, pathItems[:-1])
    except Exception as e:
        raise handle_search_dict_exceptions(path, e, 'Update')
    # This is really an upsert
    containingDict[pathItems[-1]] = value


def write_new_dict_element(dictDocument, path: str, value, newElementName=None):
    '''
    Inserts new data into the JSON document. When adding a new value to a list (array)
    newElementName should be ommitted.
    '''
    pathItems = path.split(".")[1:]
    try:
        insertLocation = search_dict(dictDocument, pathItems)
    except Exception as e:
        raise handle_search_dict_exceptions(path, e, 'Write new')
    if isinstance(insertLocation, list):
        insertLocation.append(value)
    else:
        insertLocation[newElementName] = value


def convertXpathToDictPath(path):
    text = '$' + path
    text = text.replace('/', '.')
    text = text.replace('[', '[?')

    return text

def convertXpathToDictVariable(variable, value):
    text = '{"' + variable + '": "' + value + '"}'

    return text
