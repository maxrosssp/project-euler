import sys
import math
import time

def getArea(base, size):
	baseArea = (base * (base + 1)) / 2
	return baseArea**size

def serpA(base, rows):
	if rows <= 0:
		return 0
	else:
		size = math.floor(math.log(rows, base))

		area = 0
		modSize = base**size

		print(rows),
		print(modSize)

		i = 1
		while rows >= modSize:
			area += i * getArea(base, size)

			rows -= modSize
			i += 1

		return area + (i * serpA(base, rows))


start = time.time()
print('%f' % serpA(int(sys.argv[1]), int(sys.argv[2])))
end = time.time()

print(end - start)