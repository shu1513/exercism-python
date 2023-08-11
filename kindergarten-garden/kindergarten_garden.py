class Garden:
    plantsnames = {"G": "Grass", "C": "Clover", "R": "Radishes", "V": "Violets"}

    def __init__(
        self,
        diagram,
        students=[
            "Alice",
            "Bob",
            "Charlie",
            "David",
            "Eve",
            "Fred",
            "Ginny",
            "Harriet",
            "Ileana",
            "Joseph",
            "Kincaid",
            "Larry",
        ],
    ):
        self.diagram = diagram.split("\n")
        self.students = sorted(students)

    """def plants(self, name):
        plantlist = []
        index = self.students.index(name) * 2
        for each in self.diagram:
            plantlist.append(Garden.plantsnames[each[index]])
            plantlist.append(Garden.plantsnames[each[index + 1]])
        return plantlist"""

    def plants(self, name):
        index = self.students.index(name) * 2
        return [
            Garden.plantsnames[each[i]]
            for each in self.diagram
            for i in (index, index + 1)
        ]
