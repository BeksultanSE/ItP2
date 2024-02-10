class Country:
    def __init__(self, name, population, area):
        self.name = name
        self.population = population  
        self.area = area  
        self.is_big = self.check_if_big()

    def check_if_big(self):
        return self.population > 250 or self.area > 3e6

    def population_density(self):
        return self.population / self.area

    def compare_density(self, other_country):
        if self.population_density() > other_country.population_density():
            return f"{self.name} has a larger population density than {other_country.name}"
        elif self.population_density() < other_country.population_density():
            return f"{self.name} has a smaller population density than {other_country.name}"
        else:
            return f"{self.name} and {other_country.name} have the same population density"

country1 = Country("Country A", 1000, 2e6) 
country2 = Country("Country B", 300, 7e6)  
print(country1.is_big)  
print(country2.is_big)  
print(country1.compare_density(country2))  