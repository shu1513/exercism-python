class Matrix:
    def __init__(self, matrix_string):
        self.rowlist = []
        self.columlist = []
        seperated = matrix_string.split("\n")
        for group in seperated:
            eachlist = []
            numberlist = group.split()
            for number in numberlist:
                eachlist.append(int(number))
            self.rowlist.append(eachlist)

    def row(self, index):
        return self.rowlist[index - 1]

    def column(self, index):
        for each in self.rowlist:
            self.columlist.append(each[index - 1])
        return self.columlist
