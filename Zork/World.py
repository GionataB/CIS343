class House(object):
    pass

class Neighborhood(object):
    define __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        housesList = [[]]
        for i in range(cols):
            housesList.append(House()) #Create the head of each column
        for i in range(cols):
            for j in range(1, rows):
                housesList[i].append(House()) #Create the rest of the rows

    define showNeighborhood(self):
        pass
