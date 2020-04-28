class Error(Exception):
    pass


class IDError(Error):
    def __init__(self, message):
        self.message = message
