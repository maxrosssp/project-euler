import math
# def getNextRow(previousRow):
# 	nextRow = [1]

# 	sevenDivisible = 0
# 	for i in range(1, len(previousRow)):
# 		value = previousRow[i-1] + previousRow[i]
# 		if value % 7 == 0:
# 			sevenDivisible += 1
# 		nextRow.append(value)
# 	nextRow.append(1)

# 	return nextRow, sevenDivisible

# totalDivisibleBySeven = 0


# previousRow = [1, 12, 66, 220, 495, 792, 924, 792, 495, 220, 66, 12, 1]

# for i in range(9):
# 	nextRow, s = getNextRow(previousRow)
# 	print(nextRow)
# 	previousRow = nextRow
	#nextRow, sevenDivisibleInRow = getNextRow(previousRow)
	#print '\t' + str(sevenDivisibleInRow),
	#if i % 7 == 0:
	#	print

	#totalDivisibleBySeven += sevenDivisibleInRow
	#previousRow = nextRow

#print(totalDivisibleBySeven)


def area(base):
	return (base * (base + 1)) / 2

def difference(original, base, goal):
	return base + goal

def serpAreaRec(base, size):
	if size == 0:
		return area(base) * area(base)
	else:
		return 3 * serpAreaRec(base, size - 1)

def serpArea(base, rows):
	if rows <= base:
		return area(rows)
	if rows <= base**2:
		return area(rows)
	else:
		expandedRows = rows // base // base
		print expandedRows
		size = math.floor(math.log((rows // base // base), 2))
		# print(size)
		overflow = rows - (math.pow(2, size) * math.pow(base, 2))
		return serpAreaRec(base, size) + (2 * serpArea(base, overflow))

# def serpArea(n, rows):
# 	if rows <= n:
# 		return 0
# 	else:


# def serpArea(baseSize, totalSize, goal):
# 	if baseSize >= goal:
# 		return totalSize + difference(3, baseSize, goal)
# 	else:
# 		return serpArea(baseSize * 2, totalSize * 3, goal)

import sys

# divArea = serpAreaRec(int(sys.argv[1]), int(sys.argv[2]))
divArea = serpArea(int(sys.argv[1]), int(sys.argv[2]))
print 'Area: ' + str(divArea)

print ''

# divArea, baseSize = serpArea(7, 0, 1000000000)
# totalArea = area(baseSize)
# print 'Area: ' + str(divArea)
# print 'Base size: ' + str(baseSize)
# print 'Total area: ' + str(totalArea)
# print 'Non divisible: ' + str(totalArea - divArea)