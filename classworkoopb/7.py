class IceCream:
    def __init__(self, flavor, num_sprinkles):
        self.flavor = flavor
        self.num_sprinkles = num_sprinkles

flavor_sweetness = {
    "Plain": 0,
    "Vanilla": 5,
    "ChocolateChip": 5,
    "Strawberry": 10,
    "Chocolate": 10
}

def sweetest_icecream(icecream_list):
    max_sweetness = 0
    for icecream in icecream_list:
        sweetness_value = flavor_sweetness[icecream.flavor] + icecream.num_sprinkles
        if sweetness_value > max_sweetness:
            max_sweetness = sweetness_value
    return max_sweetness

ice1 = IceCream("Chocolate", 13)
ice2 = IceCream("Vanilla", 0)
ice3 = IceCream("Strawberry", 7)
ice4 = IceCream("Plain", 18)
ice5 = IceCream("ChocolateChip", 3)

print(sweetest_icecream([ice1, ice2, ice3, ice4, ice5]))  
print(sweetest_icecream([ice3, ice1]))  
print(sweetest_icecream([ice3, ice5]))  
