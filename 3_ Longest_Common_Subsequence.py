'''
CODE CHALLENGE: Use OUTPUTLCS (reproduced below) to solve the Longest Common Subsequence Problem.
     Input: Two strings s and t.
     Output: A longest common subsequence of s and t. (Note: more than one solution may exist,
     in which case you may output any one.)

    OUTPUTLCS(backtrack, v, i, j)
        if i equals 0 or j equals 0
            return
        if backtracki, j equals"backward"
            OUTPUTLCS(backtrack, v, i minus 1, j)
        else if backtracki, j equals "forward"
            OUTPUTLCS(backtrack, v, i, j minus  1)
        else
            OUTPUTLCS(backtrack, v, i minus 1, j minus 1)
            output vi
Sample Input:
     AACCTTGG
     ACACTGTGA

Sample Output:
     AACTGG

'''


def longestCommonSubsequence(seq1, seq2):
	'''Return a longest common subsequence of the input strings'''
	lenSeq1 = len(seq1)
	lenSeq2 = len(seq2)

	S = [[0]*(lenSeq2+1) for k in xrange(lenSeq1 + 1)]

	for i in xrange(lenSeq1):
		for j in xrange(lenSeq2):

			if seq1[i] == seq2[j]:
				S[i+1][j+1] = S[i][j]+1
			else:
				S[i+1][j+1] = max(S[i+1][j], S[i][j+1])


	longestSubSeq = ''

	a = len(seq1)
	b = len(seq2)
	while a*b != 0:
		if S[a][b] == S[a-1][b]:
			a -= 1
		elif S[a][b] == S[a][b - 1]:
			b -= 1
		else:
			longestSubSeq = seq1[a-1] + longestSubSeq
			a -= 1
			b -= 1

	return longestSubSeq


'''Input/Output'''

with open('3_Longest_Common_Subsequence.txt') as inputData:
	seq1, seq2 = [line.strip() for line in inputData.readlines()] 

inputData.close()

answer = longestCommonSubsequence(seq1, seq2)
print answer

with open('3_Longest_Common_Subsequence_Answer.txt', 'w') as outputData:
	outputData.write(answer)