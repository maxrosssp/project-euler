def get_cycle_length_rec(d, r, rs):
	if r in rs:
		return len(rs) - rs.index(r)

	rs.append(r)
	return get_cycle_length_rec(d, (r * 10) % d, rs)

def get_cycle_length(d):
	if d == 0:
		return 0

	def get_cycle_length_rec(r, rs):
		if r in rs:
			return len(rs) - rs.index(r)

		rs.append(r)

		return get_cycle_length_rec((r * 10) % d, rs)

	return get_cycle_length_rec(1, [])

def get_largest_cycle_with_d_less_than(d):
	cycle_lengths = [get_cycle_length(x) for x in range(0, d)]

	return cycle_lengths.index(max(cycle_lengths))

def solution(d):
	return get_largest_cycle_with_d_less_than(d)
	
# print(get_largest_cycle_with_d_less_than(1000))