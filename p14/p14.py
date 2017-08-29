import time

def nextCollatzTerm(n):
	return n / 2 if n % 2 == 0 else (3 * n) + 1


def getCollatzSequence(n):
	sequence = []

	term = n
	while term != 1:
		sequence.append(term)
		term = nextCollatzTerm(term)

	sequence.append(1)

	return sequence


def getLongestSeqUnderMemo(n):
	sequenceDict = {
		1: 1
	}

	def getCollatzSeqLenRec(n):
		if n in sequenceDict:
			return sequenceDict[n]

		sequenceDict[n] = 1 + getCollatzSeqLenRec(nextCollatzTerm(n))

		return sequenceDict[n]

	longest = 0
	startNum = 0

	i = n
	while i > 0:
		length = getCollatzSeqLenRec(i)
		if length > longest:
			longest = length
			startNum = i
		i -= 1

	return startNum