class Education:

    def __init__(self, name="", school="", level=""):
        self.name = name
        self.school = school
        self.level = level

    def __str__(self):
        return f"Name: {self.name}, School: {self.school}, Level: {self.level}"
