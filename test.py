from candidate import Candidate
from candidate_database import CandidateDatabase
from education import Education
from experience import Experience
from main import print_candidates, print_candidate
from note import Note


def main():

    candidate_database = CandidateDatabase()

    candidate = Candidate()
    candidate.name = "Alicia Toomtest"
    candidate.title = "Python Developer"
    candidate.address = "Gothenburg, Sweden"
    candidate.phone = "0722879879"
    candidate.email = "alicia.chumchai@gmail.com"
    candidate.hobbies = "Gardening"

    candidate.education = [Education(name="Education", school="School", level="Level"),
                           Education(name="Education2", school="School2", level="Level2")]

    candidate.experience = [
        Experience(employer="Volvo", title="Python developer", responsibilities="code", duration_years="2018-present")]

    candidate.note = Note()
    candidate.note.summary = "Gslf9ehdlsdfnjslsleofjfms,"
    candidate.note.comment = "dki9eufsklwodudndjskwoeifjdk"

    # print_candidate(candidate)
    candidate_database.add_candidate(candidate)
    find_result = candidate_database.find_candidates("toom")

    if len(find_result) > 0:
        print_candidates(find_result)
    else:
        print("No result found")

    print_candidate(candidate)

    return


if __name__ == '__main__':
    main()
