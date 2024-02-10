class Person:
    def __init__(self, name, likes, hates):
        self.name = name  
        self.likes = likes  
        self.hates = hates  

    def taste(self, food_name):
        if food_name in self.likes:
            return f"{self.name} eats the {food_name} and loves it!"
        elif food_name in self.hates:
            return f"{self.name} eats the {food_name} and hates it!"
        else:
            return f"{self.name} eats the {food_name}!"

person = Person("Alice", ["pizza", "pasta"], ["broccoli", "carrots"])

print(person.taste("pizza"))  
print(person.taste("carrots"))  
print(person.taste("ice cream")) 