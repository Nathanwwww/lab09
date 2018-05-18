from src.Booking import Booking
from src.Customer import Customer
from src.Location import Location
from server import system
from src.Car import Car, SmallCar, MediumCar, LargeCar, PremiumCar
import pytest
from datetime import datetime

def generate_car_list(car_names, car_models):
    car_list = []
    car_id = 0
    for car_name in car_names:
        for car_model in car_models:
            car_list.append(SmallCar(car_name, car_model, car_id))
            car_id += 1
            car_list.append(MediumCar(car_name, car_model, car_id))
            car_id += 1
            car_list.append(LargeCar(car_name, car_model, car_id))
            car_id += 1
            car_list.append(PremiumCar(car_name, car_model, car_id))
    return car_list

user = Customer('admin', 'pass', 10)
location = Location('start_location', 'end_location')
car_list = generate_car_list(('X', 'Y', 'Z'), ('A', 'B', 'C'))
date_format = "%Y-%m-%d"
start_date = datetime.strptime("2018-12-11", date_format)
end_date = datetime.strptime("2018-12-31", date_format)
diff = end_date - start_date

def test_booking():    
  for car in car_list:
    booking = Booking(user,diff,car,location)
    assert booking.location == location
    assert booking.customer == user
    assert booking.period == diff
