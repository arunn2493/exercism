class Garden:
    def __init__(self, diagram, students=["Alice", "Bob", "Charlie", "David", "Eve", "Fred", "Ginny", "Harriet",
                                          "Ileana", "Joseph", "Kincaid", "Larry"]):
        self.diagram = diagram
        self.students = sorted(students)
        plants = {
            "V": "Violets",
            "R": "Radishes",
            "G": "Grass",
            "C": "Clover"
        }
        belonging = self.diagram.split("\n")

        r1 = [belonging[0][j:j+2] for j in range(0, len(belonging[0]), 2)]
        r2 = [belonging[1][j:j+2] for j in range(0, len(belonging[1]), 2)]

        c1 = [''.join(z) for z in zip(r1, r2)]

        self.kids_plants = {}
        for index, plant in enumerate(c1):
            temp_list = []
            for each_plant in plant:
                temp_list.append(plants[each_plant])
            self.kids_plants[self.students[index]] = temp_list

    def plants(self, students):
        return self.kids_plants[students]


garden = Garden("VCRRGVRG\nRVGCCGCV", students=[
                "Samantha", "Patricia", "Xander", "Roger"])
print(garden.plants("Patricia"))

# -------------


class Garden:
    def __init__(self, diagram, students='Alice, Bob, Charlie, David, Eve, Fred, Ginny, Harriet, Ileana, Joseph, Kincaid, Larry'.split(', ')):
        self.g = diagram.split()
        self.m = sorted(students)

    def plants(self, name):
        t = {
            'G': 'Grass',
            'C': 'Clover',
            'R': 'Radishes',
            'V': 'Violets'
        }
        i = self.m.index(name)*2

        return [t[k] for k in self.g[0][i:i+2]+self.g[1][i:i+2]]
