#you define your data collection of data
people = [
    {"name": "Harry","house": "Gryffindor"},
    {"name": "Cho","house": "Ravenclaw"},
    {"name": "Draco","house": "Slytherin"},
]

#you define to get data by name and name of collection
def f(person):
    return person["name"]

#we need sort data of this collection
#people.sort(key=f)

#declare use with labmda function
people.sort(key=lambda person: person["name"])

print(people)