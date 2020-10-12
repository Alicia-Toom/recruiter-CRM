class Experience:
    def __init__(self, employer="", title="", responsibilities="", duration_years=0):
        self.employer = employer
        self.title = title
        self.responsibilities = responsibilities
        self.duration_years = duration_years

    def __str__(self):
        return f"Employer: {self.employer}, Title: {self.title}, Responsibilities: {self.responsibilities}, Duration (Years): {self.duration_years}"
