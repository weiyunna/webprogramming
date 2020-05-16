people=[{"name":"Harry","house":"1"},
{"name":"Cho","house":"2"},
{"name":"Draco","house":"3"} ]

def f(person):
    return person["name"]

people.sort(key=f)
people.sort(key=lambda person: person["name"])

print(people)