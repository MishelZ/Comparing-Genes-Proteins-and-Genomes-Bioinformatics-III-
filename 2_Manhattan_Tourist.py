"""
CODE CHALLENGE: Find the length of a longest path in the Manhattan Tourist Problem.
Input: Integers n and m, followed by an n multiply (m plus 1) matrix Down and an (n plus 1)  multiply m matrix Right
The two matrices are separated by the symbol
Output: The length of a longest path from source (0, 0) to sink (n, m) in the n multiply m rectangular grid
whose edges are defined by the matrices Down and Right.

Sample Input:
     4 4
     1 0 2 4 3
     4 6 5 2 1
     4 4 5 2 1
     5 6 8 5 3
     -
     3 2 4 0
     3 2 4 2
     0 7 3 3
     3 3 0 2
     1 3 2 2

Sample Output:
     34
"""



def manhattan_tourist(n, m, downMatrix, rightMatrix):
	#initialize matrix to 0
	S = [[0]*(m+1) for i in xrange(n+1)]
	print S

	for i in xrange(1, n + 1):
		S[i][0] = S[i-1][0] + downMatrix[i-1][0]
	for j in xrange(1, m + 1):
		S[0][j] = S[0][j-1] + rightMatrix[0][j-1]

	for i in xrange(1, n+1):
		for j in xrange(1, m+1):
			S[i][j] = max(S[i-1][j] + downMatrix[i-1][j], S[i][j-1] + rightMatrix[i][j-1])

	return S[n][m]

'''Input/Output'''

with open('2_Manhattan_Tourist.txt') as inputData:
	n, m = map(int, inputData.readline().strip().split())
	downMatrix, rightMatrix = [[map(int, row.split()) for row in matricies.split('\n')] for matricies in inputData.read().strip().split('\n-\n')]

inputData.close()

answer = str(manhattan_tourist(n, m, downMatrix, rightMatrix)) 

print answer

with open('2_Manhattan_Tourist_Answer.txt', 'w') as outputData:
	outputData.write(answer)

	
	'''




def manhattan_tourist(row, col, down, right):
    _row = int(row) + 1
    _col = int(col) + 1
    
    mem = [[0]*_col for x in xrange(_row)]
    
    for i in range(1, _col):
        mem[0][i] = mem[0][i - 1] + right[0][i - 1]
    
    for j in range(1, _row):
        mem[j][0] = mem[j - 1][0] + down[j - 1][0]

    for i in range(1, _row):
        for j in range(1, _col):
            
            ij_down  = mem[i-1][j] + down[i-1][j]   
            ij_right = mem[i][j-1] + right[i][j-1]
                
            mem[i][j] = max(ij_down , ij_right)   

    return mem[row][col]      


def main():
    f = open('input.txt', 'r')
    
    n = int(f.readline().strip())
    m = int(f.readline().strip())
    
    down = []
    for line in f:
    
        line = line.strip()
        if line == "-":
            break
    
        down.append( map(int, line.split(" ")) )
        
    right = []
    for line in f:
        right.append( map(int, line.strip().split(" ")) )
        
    f.close()

    sol = week6.manhattan_tourist(n, m, down, right)
    
    g = open('output.txt', 'w')
    g.write(str(sol) + '\n')
    g.close()
    
if __name__ == '__main__':
    main()
	'''