
class Airplane:
    # Constructor
    def __init__(self, filled, total, row, tempFilled, seatsGrid, length):
        self.filled = filled
        self.total = total
        self.row = row
        self.tempFilled = tempFilled
        self.seatsGrid = seatsGrid
        self.length = length
        self.seats = []

    # This Function Builds and initializes the seats matrix with -1
    def construct(self):
        for ele in self.seatsGrid:
            rows = ele[1]
            cols = ele[0]
            mat = []
            for i in range(rows):
                mat.append([-1]*cols)
            self.seats.append(mat)

    # This Function fills the aisle seats by first priority
    def fillAisle_seats(self):
        self.row = 0
        self.tempFilled = -1
        while self.filled < self.total and self.filled != self.tempFilled:
            self.tempFilled = self.filled
            for i in range(self.length):
                if self.seatsGrid[i][1] > self.row:
                    if i == 0 and self.seatsGrid[i][0] > 1:
                        self.filled += 1
                        aisleCol = self.seatsGrid[i][0] - 1
                        self.seats[i][self.row][aisleCol] = self.filled
                        if self.filled >= self.total:
                            break
                    elif i == self.length - 1 and self.seatsGrid[i][0] > 1:
                        self.filled += 1
                        aisleCol = 0
                        self.seats[i][self.row][aisleCol] = self.filled
                        if self.filled >= self.total:
                            break
                    else:
                        self.filled += 1
                        aisleCol = 0
                        self.seats[i][self.row][aisleCol] = self.filled
                        if self.filled >= self.total:
                            break
                        if self.seatsGrid[i][0] > 1:
                            self.filled += 1
                            aisleCol = self.seatsGrid[i][0] - 1
                            self.seats[i][self.row][aisleCol] = self.filled
                            if self.filled >= self.total:
                                break
            self.row += 1


    # This Function fills the window seats by second priority
    def fillWindow_seats(self):
        self.row = 0 
        self.tempFilled = 0
        while self.filled < self.total and self.filled != self.tempFilled:
            self.tempFilled = self.filled
            if self.seatsGrid[0][1] > self.row:
                self.filled += 1
                window = 0
                self.seats[0][self.row][window] = self.filled
                if self.filled >= self.total:
                    break
            if self.seatsGrid[self.length-1][1] > self.row:
                self.filled += 1
                window = self.seatsGrid[self.length-1][0] - 1
                self.seats[self.length-1][self.row][window] = self.filled
                if self.filled >= self.total:
                    break
            self.row += 1

    # This Function fills the middle seats by third priority
    def fillCenter_seats(self):
        self.row = 0
        self.tempFilled = 0
        while self.filled < self.total and self.filled != self.tempFilled:
            self.tempFilled = self.filled
            for i in range(self.length):
                if self.seatsGrid[i][1] > self.row:
                    if self.seatsGrid[i][0] > 2:
                        for col in range(1, self.seatsGrid[i][0] - 1):
                            self.filled += 1
                            self.seats[i][self.row][col] = self.filled
                            if self.filled >= self.total:
                                break
            self.row += 1

    # This Function prints the seats view
    def viewSeats(self):
        for i in self.seats:
            for j in i:
                print(j)
            print()



if __name__ == "__main__":
    filled = 0
    total = 30
    row = 0
    tempFilled = -1
    seatsGrid = [[3,2], [4,3], [2,3], [3,4]]
    length = len(seatsGrid)

    obj = Airplane(filled, total, row, tempFilled, seatsGrid, length)

    # Construct
    obj.construct()

    # Aisle
    obj.fillAisle_seats()

    # Window
    obj.fillWindow_seats()

    # Center
    obj.fillCenter_seats()

    # View
    obj.viewSeats()
