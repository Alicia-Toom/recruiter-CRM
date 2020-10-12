from candidate import Candidate
from education import Education
from experience import Experience
from note import Note


def read_candidate():
    candidate = Candidate()
    candidate.name = input("Enter candidate first name and last name: ")
    candidate.title = input("Enter candidate latest title: ")
    candidate.address = input("Enter candidate address: ")
    candidate.phone = input("Enter candidate phone number: ")
    candidate.email = input("Enter candidate email address: ")
    candidate.hobbies = input("Enter candidates hobbies: ")

    choice = input("Add education? (y/n): ")
    if choice == "y":
        choice = ""
        while choice == "" or choice == "y":
            education = read_education()
            candidate.education.append(education)
            choice = input("Add additional education? (y/n): ")

    choice = input("Add experience? (y/n): ")
    if choice == "y":
        choice = ""
        while choice == "" or choice == "y":
            experience = read_experience()
            candidate.experience.append(experience)
            choice = input("Add additional experience? (y/n): ")

    choice = input("Add recruiter note (y/n): ")
    if choice == "y":
        note = read_note()
        candidate.note = note

    return candidate


def read_education():
    education = Education()
    education.name = input("Enter name of education: ")
    education.school = input("Enter name of school: ")
    education.level = input("Enter education level: ")

    return education


def read_experience():
    experience = Experience()
    experience.employer = input("Enter name of employer: ")
    experience.title = input("Enter title: ")
    experience.responsibilities = input("Enter responsibilities: ")
    experience.duration_years = int(input("Enter number of years of experience: "))

    return experience


def read_note():
    note = Note()
    note.summary = input("Enter a summary of the candidate: ")
    note.comment = input("Enter your opinion of this candidate: ")

    return note


def print_candidate(candidate):
    print(candidate)


def list_candidates(candidates):
    print(f"Number of candidates: {len(candidates)}")
    if len(candidates) > 0:
        for candidate in candidates:
            print(candidate.name)


def read_menu_option():
    print("============================")
    print("1: Add candidate")
    print("2: List candidates")
    print("3: Search candidates")
    print("4: View candidate")
    print("9: Exit")
    print("============================")

    return input("Enter your choice: ")


def main():
    candidates = []

    while True:
        choice = read_menu_option()
        if choice == "1":
            candidate = read_candidate()
            candidates.append(candidate)
        elif choice == "2":
            list_candidates(candidates)
        elif choice == "3":
            print("TODO Search Candidate")
        elif choice == "4":
            print("TODO View Candidate")
        elif choice == "9":
            break


if __name__ == '__main__':
    main()
