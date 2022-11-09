class TextLine:
    def __init__(self, text, tag, value, level, listid):
        self.text = text
        self.level = level
        self.listid = listid
        self.tag = tag
        self.value = value


class TextLines:
    def __init__(self):
        self.Lines = []

