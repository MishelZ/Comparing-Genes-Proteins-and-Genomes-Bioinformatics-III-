"""
Local Alignment Problem
Find the highest-scoring local alignment between two strings.
Given: Two protein strings.
Return: The maximum score of a local alignment of the strings, followed by a 
local alignment of these strings achieving the maximum score.
https://github.com/ngaude/sandbox/blob/f009d5a50260ce26a69cd7b354f6d37b48937ee5/bioinformatics-002/bioinformatics_chapter5.py
https://github.com/ahmdeen/Bioinformatic-Algorthims/blob/7cae61bb45535911f220da290f9ecf609b964058/Ros5F_LocalAlignment.py
"""
import os

'''Classes'''
class pam250(object):
	'''Class to score proteins using the PAM250 matrix'''

	def __init__(self):
		'''Initalize BLOSUM62 Matrix'''
		with open(os.path.join(os.path.dirname(__file__), 'PAM250.txt')) as inFile:
			lines = [line.strip().split() for line in inFile.readlines()]
			self.S = {(item[0], item[1]): int(item[2]) for item in lines} 

	def __getitem__(self, pair):
		'''Returns the score of a given pair'''
		return self.S[pair[0],pair[1]]

'''Functions'''

def localAlignment(seq1, seq2, ScoreMatrix, sig):
	'''Returns the best local Alignment of the input sequences, given a scoring matric and the indel penalty sigma'''

	len1, len2 = len(seq1), len(seq2)
	S = [[0 for j in xrange(len2+1)] for i in xrange(len1+1)]
	backtrack = [[0 for j in xrange(len2+1)] for i in xrange(len1+1)]
	maxScore = -1
	aMax, bMax = 0, 0

	for i in xrange(1, len1 +1):
		for j in xrange(1, len2+1):
			scoreList = [S[i-1][j] - sig, S[i][j-1] - sig, S[i-1][j-1] + ScoreMatrix[seq1[i-1], seq2[j-1]], 0]
			S[i][j] = max(scoreList)
			backtrack[i][j] = scoreList.index(S[i][j])

			if S[i][j] > maxScore:
				maxScore = S[i][j]
				aMax, bMax = i, j

	#------
	insertIndelFcn = lambda seq, i: seq[:i] + '-' + seq[i:]
	#------

	a, b = aMax, bMax

	align1, align2 = seq1[:a], seq2[:b]

	while backtrack[a][b] != 3 and a*b != 0:
		if backtrack[a][b] == 0:
			a -= 1
			align2 = insertIndelFcn(align2, b)
		elif backtrack[a][b] == 1:
			b -= 1 
			align1 = insertIndelFcn(align1, a)
		elif backtrack[a][b] == 2:
			a -= 1
			b -= 1 

	align1 = align1[a:]
	align2 = align2[b:]

	return str(maxScore), align1, align2 

'''Input/Output'''

with open('6_Local_Alignment_Problem.txt') as infile:
	seq1, seq2 = [line.strip() for line in infile.readlines()]

indelPenalty = 5

alignment = localAlignment(seq1, seq2, pam250(), indelPenalty)

answer = '\n'.join(alignment)
print answer

with open('6_Local_Alignment_Problem_Answer.txt', 'w') as outfile:
	outfile.write(answer)
