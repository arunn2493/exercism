# import re
# sentence = "\"That's the password: 'PASSWORD 123'!\", cried + the Special Agent.\nSo I fled."
# li = sentence.lower()
# l = re.sub("[^\d\w'\s]+'", '', li)

# print(li)
# # print(dict((i, final.count(i))for i in final))
# print(l)
# SHORTHAND_POINTS = {
#     1: "aeioulnrst",
#     2: "dg",
#     3: "bcmp",
#     4: "fhvwy",
#     5: "k",
#     8: "jx",
#     10: "qz",
# }

# POINTS = {
#     letter: value for value, letters in SHORTHAND_POINTS.items() for letter in letters
# }

# print(POINTS)

# import re
# a = "Complementary metal-oxide semiconductor"

# # print("".join(word[0].upper()
# #       for word in re.sub('_|-', '', a).split() if word != ""))
# print(re.sub('_|-', ' ', a).split())

class trial:
    def __init__(self):
        pass

    def add_student(self, name, grade):
        # if grade not in self.dict.keys():
        return set([name, ])
        # self.dict[grade].add(name)


tri = trial()
print(tri.add_student('a', 1))
print(tri.add_student('a', 1))
print(tri.add_student('c', 1))
print(tri.add_student('d', 1))
print(tri.add_student('e', 1))
