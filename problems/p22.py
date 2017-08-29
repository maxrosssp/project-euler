import time

def get_sorted_names_from_file(file_name):
	f = open(file_name, 'r')
	names = f.read()

	names = names.replace('"', '').split(',')

	names.sort()

	return names


def letter_value(letter):
	return ord(letter) - 64

def name_score(name, index):
	return reduce(lambda current_value, letter: current_value + letter_value(letter), name, 0) * index

def total_name_score(names):
	return reduce(lambda current_total, element: current_total + name_score(element[1], element[0]), enumerate(names, start=1), 0)

def old_total_name_score(names):
	total_score = 0
	for i in range(len(names)):
		total_score += name_score(names[i], i + 1)

	return total_score

def calculate_total_score(names, f, f_name):
    start = time.time()
    ans = f(names)
    end = time.time()

    print 'Got answer: %d in %f using %s' % (ans, (end - start), f_name)


names = get_sorted_names_from_file('assets/p22/names.txt')

calculate_total_score(names, total_name_score, 'total_name_score')
calculate_total_score(names, old_total_name_score, 'old_total_name_score')
