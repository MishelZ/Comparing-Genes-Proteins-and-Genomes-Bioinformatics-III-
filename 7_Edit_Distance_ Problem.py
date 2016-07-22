"""
Edit Distance Problem
Find the edit distance between two strings.
Given: Two protein strings.
Return: The edit distance between these strings.
Levenshtein introduced edit distance but did not describe an algorithm for computing it, which we leave to you.

Edit Distance Problem: Find the edit distance between two strings.
     Input: Two strings.
     Output: The edit distance between these strings.

CODE CHALLENGE: Solve the Edit Distance Problem.

Sample Input:
     PLEASANTLY
     MEANLY

Sample Output:
     5
"""


'''Functions'''

def editDist(seq1, seq2):
	'''Returns the Edit Distance between the two input strings'''

	len1, len2 = len(seq1), len(seq2)

	#Initialize Matrix

	M = [[0 for j in xrange(len2 + 1)] for i in xrange(len1+1)]
	
	#Fill out the first row and the first column of the Matrix
	for i in range(1, len1 + 1):
		M[i][0] = i 
	for j in range(1, len2 + 1):
		M[0][j] = j

	#Fill out the rest of the Matrix

	for i in xrange(1, len1 + 1):
		for j in xrange (1, len2 + 1):
			if seq1[i-1] == seq2[j-1]:
				M[i][j] = M[i-1][j-1]
			else:
				M[i][j] = min(M[i-1][j] +1, M[i][j-1] + 1, M[i-1][j-1] + 1)

	return M[len1][len2]

'''Input/Output'''

with open('7_Edit_Distance_ Problem.txt') as infile:
	seq1, seq2 = [line.strip() for line in infile.readlines()]

answer = editDist(seq1, seq2)
print str(answer)

with open('7_Edit_Distance_ Problem_Answer.txt', 'w') as outfile:
	outfile.write(str(answer))