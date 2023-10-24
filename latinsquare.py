
#import libraries
import random


# Functions creates an initial solution for latin square matrix
def generate_initial_solution(n):
    elements = [i for i in range(1, n+1) for _ in range(n)] #creates values 1 to n+1, n times   
    random.shuffle(elements) # shuffling values in elements 
    return [elements[i:i+n] for i in range(0, n*n, n)] # returns a 2-D matrix containing values from 1 to n+1  

# function to create cost of a matrix
def cost(matrix):
    n = len(matrix) # length of matrix is calculated 
    total_cost = 0
    for i in range(n):
        total_cost += (n - len(set(matrix[i])))  # calculates the number of elements missing in a row and storing it in total_cost variable
        total_cost += (n - len(set(row[i] for row in matrix)))  #  calculates the number of elements missing in a column and storing it in total_cost variable
    return total_cost

# Function that creates 3 neighbors for a latin matrix
def get_neighbors(matrix):
    n = len(matrix) # find length of matrix 
    neighbors = []

    for _ in range(3):
        x1, y1, x2, y2 = random.randint(0, n-1), random.randint(0, n-1), random.randint(0, n-1), random.randint(0, n-1) #randomly finds two position 
        while x1 == x2 and y1 == y2: # checks if both postion are same
            x1, y1, x2, y2 = random.randint(0, n-1), random.randint(0, n-1), random.randint(0, n-1), random.randint(0, n-1) # created 2 new position until 2 different position are created
        
        new_matrix = [row.copy() for row in matrix] # matrix's value are copied to new_matrix
        new_matrix[x1][y1], new_matrix[x2][y2] = new_matrix[x2][y2], new_matrix[x1][y1] # values on position (x1,y1) and (x2,y2) are swapped
        neighbors.append(new_matrix) # append the switched values to new_matrix

    return neighbors

# Function that implements simulated annealing algorithm
def simulated_annealing(n):
    matrix = generate_initial_solution(n) # initial solution is created and stored in matrix 
    best_solution = matrix 
    best_cost = cost(matrix) # cost of matrix is calculated 
    Ti = 1000
    T = Ti
    phi = 100 * n
    unchanged_count = 0
    iterations = 0

    while True:
        iterations += 1
        neighbors = get_neighbors(matrix) # neighbors of matrix are created
        next_matrix = min(neighbors, key=cost) # neighbor with minimum cost is selected
        next_cost = cost(next_matrix) #cost pf next_matrix is calculated

        # Acceptance probability
        if next_cost < best_cost: 
            best_solution, best_cost = next_matrix, next_cost # if next_cost < best_cost, best_solution and best cost is updated 
            matrix = next_matrix
        elif random.uniform(0, 1) < ((best_cost - next_cost) / T): # mathematical calculation for accpectance of a neighbour
            matrix = next_matrix

        # Cooling
        T *= 0.99

        # Stop conditions of latin matrix problem
        if best_cost == 0:
            return best_solution, iterations, "solution" 
        if int(T) <= 0:
            return best_solution, iterations, "final temperature"
        if matrix == best_solution: # if best solution is not changed then unchanged_count is updated 
            unchanged_count += 1
        else:
            unchanged_count = 0

        if unchanged_count >= phi: 
            return best_solution, iterations, "freezing factor reached"

if __name__ == "__main__":
    n = int(input("Enter a value for n (even, between 4 and 20): ")) # take value of n from user
    if n % 2 == 1 or n < 4 or n > 20:
        print("Invalid input!")
    else:
        result, iterations, stop_condition = simulated_annealing(n) # Final matrix, no. of iterations and stop conditions are found
        print("Result Matrix:")
        for row in result:
            print(row)
        print("Iterations:", iterations)
        print("Stop Condition:", stop_condition)