class CandidateDatabase:
    def __init__(self):
        self.candidates = []

    def add_candidate(self, candidate):
        candidate_id = 1
        if len(self.candidates) > 0:
            candidate_id = self.candidates[len(self.candidates) - 1] + 1

        candidate.id = candidate_id
        self.candidates.append(candidate)

    def get_candidate(self, candidate_id):
        for candidate in self.candidates:
            if str(candidate.id) == str(candidate_id):
                return candidate

    def get_candidates(self):
        return self.candidates

    def find_candidates(self, search_criteria):
        result = []
        for candidate in self.candidates:
            if search_criteria.lower() in candidate.name.lower():
                result.append(candidate)
            elif search_criteria.lower() in candidate.title.lower():
                result.append(candidate)

        return result
