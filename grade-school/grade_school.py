class School:
    def __init__(self):
        self.dict = {}

    def add_student(self, name, grade):
        if grade not in self.dict.keys():
            self.dict[grade] = set([name, ])
        self.dict[grade].add(name)

    def roster(self):
        temp = []
        for k in sorted(self.dict.keys()):
            temp.extend(sorted(list(self.dict[k])))
        return temp

    def grade(self, grade_number):
        if grade_number in self.dict.keys():
            return sorted(self.dict[grade_number])
        return []
