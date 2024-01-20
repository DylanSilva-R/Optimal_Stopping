from parkingLotObject import *
from calculationsObject import *

def main():

    print("---------------------------------------")
    print("|Optimal stopping calculator (parking)|")
    print("---------------------------------------")
    print("")
    
    loop = True
    countIterations = 0
    successCount = 0
    
    ParkingSpacesValue = parkingSpaces()
    print("")
    
    PL = parkingLot(ParkingSpacesValue) # ParkingLot object
    print("")

    print("Your randomly generated parking lot is being created...")
    print(PL.create_Random_Matrices())

    print("Your randomly filled parking lots: ")

    updatedMatrix = PL.random_Fill()
    print(updatedMatrix)


    updatedMatrix = PL.random_Fill()
    print(updatedMatrix)

    newM = PL.random_Fill()
    print(newM)

    


    """
    for i in range(100):
        countIterations+=1
        #print("")

        print("Your parking lot is being randomly being filled out...")
        matrix = PL.random_Fill()
        print(matrix)

        calc = calculations(ParkingSpacesValue)
        k = calc.optimalStoppingCalc()
        successCount += int(PL.travel_The_Matrix(k))

        print("")
        #loop = end_Simulation()
    
    successRate = round((successCount / countIterations) * 100, 2)
    print("Your sucess rate of finding a parking spot is " + str(successRate) + "%")
    """

def parkingSpaces():
    while True:
        try:
            parkingSpaces =  int(input("How many parking spaces are you surrounded by? ")) # This value will help use create a matrix of parking lots.
            print("Your value will be used to create a random parking lot.")
            break
        except ValueError:
            print("Invalid input. Please try again.\n")
            continue

    return parkingSpaces

def end_Simulation():    
    while True:
        endSimulation = input("Do you want to keep experimenting? (Y or N): ")

        if endSimulation == "Y":
            Option = True
            break
        elif endSimulation == "N":
            Option = False
            break
        else:
            print("You didn't input the right option man. Please try again.\n")
            continue
    return Option

main()
