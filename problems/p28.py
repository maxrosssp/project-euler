def get_diagonal_sum_size(w):
	count = (w + 1) / 2

	total = 1
	current_number = 1
	for i in range(1, count):

		dist = (i) * 2

		for corner in range(4):
			current_number += dist

			total += current_number

	return total

print(get_diagonal_sum_size(1001))