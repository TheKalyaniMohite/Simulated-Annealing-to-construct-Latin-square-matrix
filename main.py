from latin_square import simulated_annealing

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