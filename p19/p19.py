def is_leap_year(year):
	if year % 4 != 0:
		return False

	if year % 400 == 0:
		return True

	if year % 100 == 0:
		return False

	return True

# def thirty_day_month(year):
# 	return 30

# def thirty_one_day_month(year):
# 	return 31

# def february(year):
# 	return 29 if is_leap_year(year) else 28

sunday_firsts_for_year_starting_with = {
	0: 2,
	1: 2,
	2: 2,
	3: 1,
	4: 3,
	5: 1,
	6: 1
}

sunday_firsts_for_leap_year_starting_with = {
	0: 3,
	1: 2,
	2: 1,
	3: 2,
	4: 2,
	5: 1,
	6: 1
}

def sunday_firsts_until(end_year):
	day = 1
	year = 1900

	sunday_firsts = 0

	while year < end_year:
		if is_leap_year(year):
			sunday_firsts += sunday_firsts_for_leap_year_starting_with[day]
			day += 2
		else:
			sunday_firsts += sunday_firsts_for_year_starting_with[day]
			day += 1

		day %= 7
		year += 1

	return sunday_firsts


print(sunday_firsts_until(2001) - sunday_firsts_until(1901))


# days_in_month = {
# 	0: thirty_one_day_month,
# 	1: february,
# 	2: thirty_one_day_month,
# 	3: thirty_day_month,
# 	4: thirty_one_day_month,
# 	5: thirty_day_month,
# 	6: thirty_one_day_month,
# 	7: thirty_one_day_month,
# 	8: thirty_day_month,
# 	9: thirty_one_day_month,
# 	10: thirty_day_month,
# 	11: thirty_one_day_month
# }

# days_in_month = {
# 	'Jan': thirty_one_day_month,
# 	'Feb': february,
# 	'Mar': thirty_one_day_month,
# 	'Apr': thirty_day_month,
# 	'May': thirty_one_day_month,
# 	'Jun': thirty_day_month,
# 	'Jul': thirty_one_day_month,
# 	'Aug': thirty_one_day_month,
# 	'Sep': thirty_day_month,
# 	'Oct': thirty_one_day_month,
# 	'Nov': thirty_day_month,
# 	'Dec': thirty_one_day_month
# }

# months_of_year = {
# 	0: 'Jan',
# 	1: 'Feb',
# 	2: 'Mar',
# 	3: 'Apr',
# 	4: 'May',
# 	5: 'Jun',
# 	6: 'Jul',
# 	7: 'Aug',
# 	8: 'Sep',
# 	9: 'Oct',
# 	10:'Nov',
# 	11:'Dec'
# }

# days_of_week = {
# 	0: 'Sun',
# 	1: 'Mon',
# 	2: 'Tue',
# 	3: 'Wed',
# 	4: 'Thu',
# 	5: 'Fri',
# 	6: 'Sat'
# }

# def print_date(day_of_week, month_of_year, year):
# 	print '%s %d: %s' % (months_of_year[month_of_year], year, days_of_week[day_of_week])

# def get_day_of_week(end_month, end_year):
# 	day = 1
# 	year = 1900

# 	sundays = 0
# 	while year < end_year:
# 		for month in range(12):
# 			# print_date(day, month, year)

# 			day += days_in_month[month](year)
# 			day %= 7

# 			if day == 0:
# 				sundays += 1

# 		year += 1

# 	for month in range(end_month):
# 		print_date(day, month, year)

# 		day += days_in_month[month](year)
# 		day %= 7

# 		if day == 0:
# 			sundays += 1

# 	return sundays

# print(get_day_of_week(12, 1904))
# print(get_day_of_week(12, 2000) - get_day_of_week(11, 1901))

# for year in [1901, 1904, 1907, 1908, 1992, 1996, 2000]:
# 	print '%d: %s' % (year, 'YES' if is_leap_year(year) else 'NO')


