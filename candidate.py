import random

class Candidate:

    def __init__(self, name="", title="", address="", phone="", email="", hobbies ="", education=[], experience=[], note=None):

        self.name = name
        self.title = title
        self.address = address
        self.phone = phone
        self.email = email
        self.hobbies = hobbies
        self.education = education
        self.experience = experience
        self.note = note

    def __str__(self):
        return f"Name: {self.name}, Title: {self.title}, Address: {self.address}, Phone: {self.phone}, E-Mail: {self.email}, Hobbies: {self.hobbies}"

