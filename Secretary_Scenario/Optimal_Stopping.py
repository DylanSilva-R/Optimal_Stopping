import math
import random as rand

def fill_Candidate_Array(candidate_Array, candidate_Ranking, candidate_Pool_Size):

    rand.shuffle(candidate_Ranking)

    for i in range(candidate_Pool_Size):
        candidate_Array[i] = candidate_Ranking[i]
    
    return candidate_Array

def optimal_Stopping_Calculation(candidates):
    
    e = 2.71828
    k = round(candidates / e)

    return k


def choose_candidate(candidate_Array):
    k = optimal_Stopping_Calculation(len(candidate_Array))

    max_rank = 0
    for i in range(0,k):
        max_rank = max(max_rank,candidate_Array[i])
    
    for i in range(k,len(candidate_Array)-1):
        if candidate_Array[i] > max_rank:
            return i


    return len(candidate_Array)-1

def probability_Of_Success(candidates, optimal_Size): # Probability of success calculation.
    x = optimal_Size / candidates
    prob_Success = -x*math.log(x)

    return round(prob_Success, 2) * 100

def good_Cand_Bad_Cand(candidate_Array, stop): # This function will determine if the candidate choice is good or not.
    max_index = 0
    for i in range(1,len(candidate_Array)):
        if candidate_Array[i] > candidate_Array[max_index]:
            max_index = i
    return i == stop

def __main__():

    candidate_Pool = rand.randint(1, 50)
    print("Candidate pool: " + str(candidate_Pool))
    
    candidate_Potential_Ratings = list(range(1,candidate_Pool + 1))

    candidate_Array = [0] * candidate_Pool
    
    iterations = 10000
    success_Count = 0

    print("An array of " + str(candidate_Pool) + " candidates will be created. This program will run " + str(iterations) + " times, and the candidates will be randomly ranked every iteration.")
    optimal_Stop = optimal_Stopping_Calculation(candidate_Pool)
    print("You should stop rejecting and start hiring after observing " + str(optimal_Stop) + " candidates")
    print("Probability of success : " + str(probability_Of_Success(candidate_Pool, optimal_Stop)) +"%")


    for i in range(iterations):

        candidate_Array = fill_Candidate_Array(candidate_Array, candidate_Potential_Ratings, candidate_Pool)
        chosen = choose_candidate(candidate_Array)
        success_Count += good_Cand_Bad_Cand(candidate_Array, chosen)

    success_Rate = round((success_Count / iterations) * 100, 2)
    print("Your actual success rate: " + str(success_Rate) + "%")

__main__()
