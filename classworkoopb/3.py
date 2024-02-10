class Composer:
    count = 0  
    def __init__(self, name, dob, country):
        self.name = name
        self.dob = dob  
        self.country = country  
        Composer.count += 1

composer1 = Composer("Ludwig van Beethoven", "1770-12-17", "Germany")
print(Composer.count)  

composer2 = Composer("Wolfgang Amadeus Mozart", "1756-01-27", "Austria")
print(Composer.count)  

composer3 = Composer("Johann Sebastian Bach", "1685-03-31", "Germany")
print(Composer.count)
