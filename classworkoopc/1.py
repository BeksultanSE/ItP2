class Person:
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
    
    def __repr__(self):
        return f"{self.firstname} {self.lastname}"

def people_sort(people, attribute):
    return sorted(people, key=lambda person: getattr(person, attribute))

p1 = Person("Michael", "Smith", 40)
p2 = Person("Alice", "Waters", 21)
p3 = Person("Zoey", "Jones", 29)

sort_by_firstname = people_sort([p1, p2, p3], "firstname")
sort_by_lastname = people_sort([p1, p2, p3], "lastname")
sort_by_age = people_sort([p1, p2, p3], "age")

print(sort_by_firstname, sort_by_lastname, sort_by_age, sep='\n')
