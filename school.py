class School():
    def __init__(self, name=None):
        self.name = name
        self.roster = {}
        pass

    def add_student(self, student, grade):
        if grade in self.roster.keys():
            self.roster[grade].append(student)
        else:
            self.roster[grade] = [student]
    
    def grade(self, grade):
        
        if grade in self.roster.keys():
            return list(self.roster[grade])
        else:
            return "Grade not found"
    
    def sort_roster(self):
        sorted_roster = {}
        for grade in self.roster.keys():
            sorted_roster[grade] = sorted(list(self.roster[grade]))
        return sorted_roster
