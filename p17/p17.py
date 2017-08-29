numberToWord = {
	0: '',
	1: 'one',
	2: 'two',
	3: 'three',
	4: 'four',
	5: 'five',
	6: 'six',
	7: 'seven',
	8: 'eight',
	9: 'nine',
	10: 'ten',
	11: 'eleven',
	12: 'twelve',
	13: 'thirteen',
	14: 'fourteen',
	15: 'fifteen',
	16: 'sixteen',
	17: 'seventeen',
	18: 'eighteen',
	19: 'nineteen',
	20: 'twenty',
	30: 'thirty',
	40: 'forty',
	50: 'fifty',
	60: 'sixty',
	70: 'seventy',
	80: 'eighty',
	90: 'ninety',
	100: 'hundred',
	1000: 'thousand'
}

numberWordLengths = {
	0: 0, 1: 3, 2: 3, 3: 5, 4: 4, 5: 4, 6: 3, 7: 5, 8: 5, 9: 4, 10: 3, 
	11: 6, 12: 6, 13: 8, 14: 8, 15: 7, 16: 7, 17: 9, 18: 8, 19: 8, 
	20: 6, 30: 6, 40: 5, 50: 5, 60: 5, 70: 7, 80: 6, 90: 6, 
	100: 7, 
	1000: 8,
	'and': 3
}

def numberLetterCount(number):
	count = 0

	if number >= 1000:
		count += numberWordLengths[number / 1000] + numberWordLengths[1000]
		number %= 1000

	if number >= 100:
		count += numberWordLengths[number / 100] + numberWordLengths[100]
		number %= 100
		if number > 0: 
			count += 3

	if number <= 20:
		count += numberWordLengths[number]
	elif number > 0:
		count += numberWordLengths[(number / 10) * 10] + numberWordLengths[number % 10]

	return count

def numberLetterCount2(number):
	count = 0

	if number >= 1000:
		count += len(numberToWord[number / 1000]) + len(numberToWord[1000])
		number %= 1000

	if number >= 100:
		count += len(numberToWord[number / 100]) + len(numberToWord[100])
		number %= 100
		if number > 0: 
			count += 3

	if number <= 20:
		count += len(numberToWord[number])
	elif number > 0:
		count += len(numberToWord[(number / 10) * 10]) + len(numberToWord[number % 10])

	return count


def numberWord(number):
	word = ''

	if number >= 1000:
		word += numberToWord[number / 1000] + ' ' + numberToWord[1000] + ' '
		number %= 1000

	if number >= 100:
		word += numberToWord[number / 100] + ' ' + numberToWord[100] + ' '
		number %= 100
		if number > 0: 
			word += 'and ' 

	if number > 20:
		word += numberToWord[(number / 10) * 10] + ' ' + numberToWord[number % 10]
	elif number > 0:
		word += numberToWord[number]

	return word.strip()


def sumNumberLetterCounts(n):
	return reduce((lambda total, n: total + numberLetterCount(n)), range(1, n + 1), 0)

