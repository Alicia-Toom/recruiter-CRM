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
    education.school = input("Enter name of school/university: ")
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

    print_section_header("General Information")
    print(f"Name: {candidate.name}")
    print(f"Title: {candidate.title}")
    print(f"Address: {candidate.address}")
    print(f"Address: {candidate.address}")
    print(f"Phone: {candidate.phone}")
    print(f"E - Mail: {candidate.email}")
    print(f"Hobbies: {candidate.hobbies}")
    print_section_header("Summary")
    print(f"Summary: {candidate.note.summary}")
    print_section_header("Education")
    for education in candidate.education:
        print(f"Education: {education.name}")
        print(f"School/University: {education.school}")
        print(f"Level: {education.level}")
    print_section_header("Job Experience")
    for experience in candidate.experience:
        print(f"Employer: {experience.employer}")
        print(f"Title: {experience.title}")
        print(f"Responsibilities: {experience.responsibilities}")
        print(f"Duration: {experience.duration_years}")
    print_section_header("Recruiter Notes")
    print(f"Note: {candidate.note.comment}")


def print_section_header(header):
    print("-----------------------------")
    print(f"{header.upper()}")
    print("-----------------------------")


def find_candidates(candidates, search_criteria):

    result = []
    for candidate in candidates:
        if search_criteria.lower() in candidate.name.lower():
            result.append(candidate)
        elif search_criteria.lower() in candidate.title.lower():
            result.append(candidate)

    return result


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


def test():

    candidate = Candidate()
    candidate.name = "Alicia Toomtest"
    candidate.title = "Python Developer"
    candidate.address = "Gothenburg, Sweden"
    candidate.phone = "0722879879"
    candidate.email = "alicia.chumchai@gmail.com"
    candidate.hobbies = "Gardening"

    candidate.education = [Education(name="Education", school="School", level="Level"), Education(name="Education2", school="School2", level="Level2")]

    candidate.experience = [Experience(employer="Volvo", title="Python developer", responsibilities="code", duration_years="2018-present")]

    candidate.note = Note()
    candidate.note.summary = "Gslf9ehdlsdfnjslsleofjfms,"
    candidate.note.comment = "dki9eufsklwodudndjskwoeifjdk"

    #print_candidate(candidate)
    candidates = [candidate]
    find_result = find_candidates(candidates, "toom")

    if len(find_result) > 0:
        list_candidates(find_result)
    else:
        print("No result found")
    return


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
            search_term = input("Please enter candidates name or title: ")
            find_result = find_candidates(candidates, search_term)
            if len(find_result) > 0:
                list_candidates(find_result)
            else:
                print("No Candidate found")
        elif choice == "4":
            print("TODO View Candidate")
        elif choice == "9":
            break


if __name__ == '__main__':
    main()
