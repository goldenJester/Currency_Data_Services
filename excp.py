class NoFileFoundException(Exception):
    statuscode = 404

    def __init__(self, msg):
        super().__init__(f"{self.__class__.__name__} : {msg}")

class NoDataAvailableException(Exception):
    statuscode = 404

    def __init__(self, msg):
        super().__init__(f"{self.__class__.__name__} : {msg}")

class ParsingDictionaryError(Exception):

    def __init__(self, msg):
        super().__init__(f"{self.__class__.__name__} : {msg}")