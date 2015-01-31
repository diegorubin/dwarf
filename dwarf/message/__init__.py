import re

class Message(object):
    def __init__(self, message):
        self.__message = message

    def links(self):
        link_pattern = re.compile('(([a-z]+:\/\/)?([\w]+\.[\w\.]+\w))')
        groups = link_pattern.findall(self.__message)
        return [group[0] for group in groups]

