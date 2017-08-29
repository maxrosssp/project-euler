import numpy as np

def latticePathsForGrid(height, width):
	memoTable = np.ones((height + 1, width + 1))
	
	for x in range(1, height + 1):
		for y in range(x, width + 1):
			if x == y:
				memoTable[x, y] = 2 * memoTable[x - 1, y]
			else:
				memoTable[x, y] = memoTable[x, y -1] + memoTable[x - 1, y]

	return memoTable[height, width]


# def latticePathsRec(x, y):
# 	if x == 0 or y == 0:
# 		return 1
# 	else:
# 		return latticePathsRec(x, y - 1) + latticePathsRec(x - 1, y)