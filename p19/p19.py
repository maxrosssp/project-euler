def isLeapYear(year):
	if year % 4 != 0:
		return False

	if year % 400 == 0:
		return True

	if year % 100 == 0:
		return False

	return True

def thirty_day_month(year):
	return 30

def thirty_one_day_month(year):
	return 31

def february(year):
	return 29 if isLeapYear(year) else 28

days_in_month = {
	0: thirty_one_day_month,
	1: february,
	2: thirty_one_day_month,
	3: thirty_day_month,
	4: thirty_one_day_month,
	5: thirty_day_month,
	6: thirty_one_day_month,
	7: thirty_one_day_month,
	8: thirty_day_month,
	9: thirty_one_day_month,
	10: thirty_day_month,
	11: thirty_one_day_month
}

days_of_week = {
	0: 'Sunday',
	1: 'Monday',
	2: 'Tuesday',
	3: 'Wednesday',
	4: 'Thursday',
	5: 'Friday',
	6: 'Saturday'
}

def get_day_of_week(end_month, end_year):
	day = 1
	month = 0
	year = 1900

	sundays = 0
	while year < end_year:
		for i in range(12):
			day = (day + days_in_month[month](year)) % 7

			if day == 0:
				sundays += 1
		year += 1

	for i in range(end_month):
		day = (day + days_in_month[month](year)) % 7

		if day == 0:
			sundays += 1

	return sundays


print(get_day_of_week(11, 2000) - get_day_of_week(11, 1901))
