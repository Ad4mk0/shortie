class NoAccess(Exception):
    """Exception raised for errors with access.

    Attributes:
        message -- explanation of the error
    """
    def __init__(self, message="Lol"):
        self.message = message
        super().__init__(self.message)