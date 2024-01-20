import numpy as np
import random

class parkingLot:
    def __init__(self, parkingSpots):
        self.parkingSpots = parkingSpots
        
    def create_Random_Matrices(self):
        potentialRows = []
        potentialColumns = []

        for i in range(1, self.parkingSpots + 1):
            if self.parkingSpots % i == 0:
                potentialRows.append(i)
                potentialColumns.append(self.parkingSpots / i)

        size = len(potentialColumns)

        randChoice = random.randint(0, size - 1)

        self.rows = int(potentialRows[randChoice])
        self.columns = int(potentialColumns[randChoice])

        self.matrix = np.full([self.rows, self.columns], 0, dtype=int)
        return self.matrix

    def random_Fill(self):
        randomParkedCars = random.randint(1, self.parkingSpots)  # Random parked cars.
        print("There are " + str(randomParkedCars) + " parked in the parking lot.\n")
        count = 0

        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                if count < randomParkedCars:
                    self.matrix[i][j] = 1
                    count += 1
                else:
                    break

        return self.matrix

    def travel_The_Matrix(self, stop):
        count = 0
        store = 0
        rStore = 0
        cStore = 0
        
        print("You should stop looking for parking after checking " + str(stop) + " parking spots")

        for i in reversed(range(len(self.matrix))):
            for j in reversed(range(len(self.matrix[i]))):
                if count != stop:
                    print(str(self.matrix[i][j])+ " = location ["+str(i)+"]["+str(j))
                    count += 1
                elif count == stop:
                    store = self.matrix[i][j]
                    c_store = j  # location of column
                    r_store = i  # location of row
                    break

        if store == 1:
            print("You did not find a parking spot at location [" + str(rStore) + "][" + str(cStore) + "]")
            return 1
        else:
            print("You found a parking spot at location [" + str(rStore) + "][" + str(cStore) + "]")
            return 0
        
    