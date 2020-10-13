#!/usr/bin/env python3
import json

content = []
with open("data.json") as data:
	content = json.load(data)
people = [{'name': 'Pontus', 'age': 30},
		{'name': 'Sara', 'age': 29},
		{'name': 'Sara', 'age': 28},
		{'name': 'Sara', 'age': 27},
		{'name': 'Sara', 'age': 26},
		{'name': 'Sara', 'age': 25},
		{'name': 'Sara', 'age': 24},
		{'name': 'Sara', 'age': 23},
		{'name': 'Sara', 'age': 22},
		{'name': 'Sara', 'age': 21},
		{'name': 'Sara', 'age': 20},
		{'name': 'Xavier', 'age': 19}]

people2 = [{'name': 'Pontus', 'age': 30},
		{'name': 'Sara', 'age': 28},
		{'name': 'Sara', 'age': 27},
		{'name': 'Sara', 'age': 24},
		{'name': 'Sara', 'age': 26},
		{'name': 'Sara', 'age': 29},
		{'name': 'Sara', 'age': 23},
		{'name': 'Sara', 'age': 22},
		{'name': 'Sara', 'age': 25},
		{'name': 'Sara', 'age': 20},
		{'name': 'Sara', 'age': 21},
		{'name': 'Xavier', 'age': 19}]
#print(people, "\n\n")

#6a
def linear_search(haystack, needle, filt=lambda e: " ".join([str(item[1]) for item in e.items()])):
	for straw in haystack:
		if str(needle).lower() in str(filt(straw)).lower():
			return straw

#		if len(haystack) == 1:
#			if str(haystack[0]).lower() == needle:
#				return haystack[0]
#		else:
#6b
def binary_search(haystack, needle, filt = None):
	if len(haystack) == 1:
		if haystack[0] == needle:
			return haystack[0]
		else:
			return None
	if not filt:
		for key in haystack[0].keys():
			awnser = binary_search(haystack, needle, lambda e: e[key])
			if awnser:
				return awnser
	else:
		middle = int(len(haystack)/2)
		needle = str(needle)
		middle_straw = str(filt(haystack[middle]))
		if needle == middle_straw:
			return haystack[middle]
		elif needle > middle_straw:
			return binary_search(haystack[:middle], needle, filt)
		elif needle < middle_straw:
			return binary_search(haystack[middle:], needle, filt)

def main():
	#print(linear_search(content, 9000, filt = lambda e: e['lulz_had']))

	print("Hello", binary_search(people2, 19))
	#print(insertion_sort(people2, lambda e: e['age']))

if __name__ == "__main__":
	main()
