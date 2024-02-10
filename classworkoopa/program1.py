class BasicPlan:
    can_stream = True
    can_download = True
    has_SD = True
    num_of_devices = 1
    price = 8.99
class StandardPlan(BasicPlan):
    has_HD = True
    num_of_devices = 2
    price = 12.99
class PremiumPlan(StandardPlan):
    has_UHD = True
    num_of_devices = 4
    price = 15.99

print(BasicPlan.can_download)
print(BasicPlan.price)

print(StandardPlan.can_download)
print(StandardPlan.price)

print(PremiumPlan.can_download)
print(PremiumPlan.price)

    
    