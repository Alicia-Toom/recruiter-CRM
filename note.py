class Note:

    def __init__(self, summary="", comment=""):
        self.summary = summary
        self.comment = comment

    def __str__(self):
        return f"Summary: {self.summary}, Comment: {self.comment}"