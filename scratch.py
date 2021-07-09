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

import re
a = "Complementary metal-oxide semiconductor"

# print("".join(word[0].upper()
#       for word in re.sub('_|-', '', a).split() if word != ""))
print(re.sub('_|-', ' ', a).split())
