import random

from project.src.entities.User import User
from project.src.service.VehicleDealer import VehicleDealer


def initialize_vehicle_dealer():
    vehicle_dealer: VehicleDealer = VehicleDealer()
    if len(vehicle_dealer.get_users_list()) == 0:
        print('No users right now. Proceding to create a new one...')
        user_id = random.Random
        name = _read_value_from_prompt('name')
        surnames = _read_value_from_prompt('surnames')
        password = _read_value_from_prompt('password')
        vehicle_dealer.add_user(User(user_id, name, surnames, password))


def _read_value_from_prompt(required_value):
    value = None
    while value is None or len(value) == 0:
        value = input('Please, write your ' + required_value + ': ')
    return value


if __name__ == '__main__':
    initialize_vehicle_dealer()
