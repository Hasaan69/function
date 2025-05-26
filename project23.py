def trip(days,person):
    hotel=120*days
    plane=1500*person
    vehicle=400*days
    total=hotel+plane+vehicle
    return hotel
print('total cost price=',trip(5,4))