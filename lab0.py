import datetime
date = datetime.datetime.now()
name = input("Vad heter du:")
print("Hej ", name + "!")
age = int(input("Mata in din ålder: "))
print("Du föddes år", date.year-age)
county = input("Vilket län föddes du i: ")
print("\nFörsta halvan av ditt namn och andra halvan av ditt län är:", name[0:int(len(name)/2)] + county[int(len(county)/2):len(county)])
