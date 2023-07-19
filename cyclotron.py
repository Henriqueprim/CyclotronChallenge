import time


def cyclotron(particle, matrix):
    if particle == 'n':
        # First line is replaced with same sized list filled with 'n'
        matrix[0] = ['n'] * len(matrix[0])
        return matrix
    elif particle == 'e':
        # First line is replaced with same sized list filled with 'e'
        matrix[0] = ['e'] * len(matrix[0])

        # For each line in the matrix
        for i in range(0, len(matrix)):
            # replace the item in the last position with 'e'
            matrix[i][-1] = 'e'
        return matrix
    elif particle == 'p':
        # First line is replaced with same sized list filled with 'p'
        matrix[0] = ['p'] * len(matrix)

        # Last line is replaced with same sized list filled with 'p'
        matrix[-1] = ['p'] * len(matrix)

        # For each line in the matrix
        for i in range(0, len(matrix)):
            # replace the item in the first position with 'p'
            matrix[i][0] = 'p'

            # replace the item in the last position with 'p'
            matrix[i][-1] = 'p'

        # replace the last item in the matrix back to 1
        matrix[-1][-1] = 1

        # replace the next to last item in the matrix with 'p'
        matrix[-2][-2] = 'p'
        return matrix


n = 4
matrix = [[1 for j in range(n)] for i in range(n)]

start_time = time.time()
result = cyclotron("n", matrix)
print(result)
result = cyclotron("e", matrix)
print(result)
result = cyclotron("p", matrix)
print(result)
end_time = time.time()

print("Elapsed time: %2.5fs" % (end_time - start_time))
