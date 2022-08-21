import json
import logging
import random
from os import system, name

import requests
from singleton_decorator import singleton

from project.src.entities.Bus import Bus
from project.src.entities.Proprietary import Proprietary
from project.src.entities.Sale import Sale
from project.src.entities.Truck import Truck
from project.src.entities.User import User
from project.src.entities.Van import Van
from project.src.entities.Vehicle import Vehicle

URL = "http://127.0.0.1:8000/users"


def _print_truck_info_if_is_truck(vehicle):
    if isinstance(vehicle, Truck):
        print('TARA: ' + vehicle.tara)
        print('Maximum authorized charge: ' + vehicle.maximum_auth_charge)
        print('Number of wheels: ' + vehicle.number_of_wheels)


def _print_common_vehicle_info_without_starter(vehicle):
    print('Register number: ' + vehicle.get_register_number())
    print('Brand: ' + vehicle.brand)
    print('Model: ' + vehicle.model)
    print('Buy date: ' + vehicle.get_buy_date())
    print('Build date: ' + vehicle.get_build_date())
    print('Color: ' + vehicle.color)
    print('Kilometers: ' + vehicle.kilometers)
    if len(vehicle.observations) != 0:
        print('Observations:')
        for index, observation in enumerate(vehicle.observations):
            print(str(index) + ": " + observation)


def _print_common_sale_info(sale):
    print('=============================================')
    print('Sale date: ' + sale.sale_date)
    _print_common_vehicle_info_without_starter(sale.vehicle)


def _clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux
    else:
        _ = system('clear')


def _print_common_vehicle_info(vehicle):
    print('=============================================')
    _print_common_vehicle_info_without_starter(vehicle)


def _print_bus_info_if_is_bus(vehicle):
    if isinstance(vehicle, Bus):
        print("Number of passengers: " + vehicle.passenger_number)
        print("Video: " + vehicle.video.name)
        print("Number of wheels: " + vehicle.number_of_wheels)


def _print_van_info_if_is_van(vehicle):
    if isinstance(vehicle, Van):
        print('Load volume: ' + vehicle.load_volume)
        print('Maximum load length: ' + vehicle.load_longitude)


def _print_user_info(user):
    print('=============================================')
    print('User code: ' + user.get_user_code())
    print('Name: ' + user.get_name())
    print('Surnames: ' + user.get_surnames())


def _print_end_line_and_wait_for_enter():
    print('=============================================\n')
    input('Press <Enter> to continue')


class BackEndException(Exception):
    pass


@singleton
class VehicleDealer:
    """
    Esta clase utiliza un patrón de diseño singleton.
    Contiene 3 atributos; son List de tipos usuario, vehículo y venta.
    Estas listas almacenarán todos los datos del concesionario.
    """

    @classmethod
    def __init__(cls):
        cls.user_list = list()
        cls.sales_list = list()
        cls.vehicle_list = list()

    @classmethod
    def add_vehicle(cls, vehicle: Vehicle):
        cls.vehicle_list.append(vehicle)

    @classmethod
    def remove_vehicle(cls, register_number):
        for index, vehicle in enumerate(cls.vehicle_list):
            if vehicle.get_register_number() == register_number:
                cls.vehicle_list.remove(index)
        logging.error('Vehicle with ID %s not found', register_number)

    @classmethod
    def show_showroom_vehicle_info(cls, register_number):
        vehicle = cls.get_showroom_vehicle(register_number)
        if vehicle is not None:
            _print_common_vehicle_info(vehicle)
            _print_truck_info_if_is_truck(vehicle)
            _print_bus_info_if_is_bus(vehicle)
            _print_van_info_if_is_van(vehicle)
            _print_end_line_and_wait_for_enter()

    @classmethod
    def get_vehicle_list(cls):
        if len(cls.vehicle_list) == 0:
            print('No vehicles in showroom')
            input('Press <Enter> to continue')
        else:
            for vehicle in cls.vehicle_list:
                _print_common_vehicle_info(vehicle)
                _print_end_line_and_wait_for_enter()
                _clear()

    @classmethod
    def get_showroom_vehicle(cls, register_number):
        for vehicle in cls.vehicle_list:
            if vehicle.get_register_number() == register_number:
                return vehicle
        logging.error('Vehicle with ID %s not found', register_number)

    @classmethod
    def add_user(cls, user: User):
        user_id = user.get_user_code()
        while requests.get(URL + "/" + user_id).status_code == 200:
            user_id = str(random.randrange(1000, 9999))
        user.set_user_code(user_id)
        create_user_req = requests.post(URL, json=json.dumps(user))
        if create_user_req.status_code == 201:
            create_user_req = create_user_req.json()
            user = User(create_user_req.user_code, create_user_req.name, create_user_req.surnames)
            return user
        elif create_user_req.status_code == 200:
            return None
        else:
            raise BackEndException("Cannot connect with backend")

    @classmethod
    def delete_user(cls, user_id):
        for index, user in enumerate(cls.user_list):
            if user.get_user_code() == user_id:
                cls.user_list.remove(index)
        logging.error('User with ID %s not found', user_id)

    @classmethod
    def get_users_list(cls):
        if len(cls.user_list) == 0:
            print('No users')
            input('Press <Enter> to continue')
        else:
            for index, user in enumerate(cls.user_list):
                _print_user_info(user)
                if index % 2 != 0:
                    _print_end_line_and_wait_for_enter()
                    _clear()
                else:
                    print('=============================================')

    @classmethod
    def get_user_info(cls, user_id):
        for user in cls.user_list:
            if user.get_user_code() == user_id:
                _print_user_info(user)
                _print_end_line_and_wait_for_enter()

    @classmethod
    def auth_user(cls, user_id, pwd):
        body = {"client_id": user_id, "client_secret": pwd}
        auth_request = requests.post("%s/auth" % URL, json=json.dumps(body))
        if auth_request.status_code == 200:
            auth_request = auth_request.json()
            user = User(auth_request.user_code, auth_request.name, auth_request.surnames)
            return user
        logging.error('User with ID %s not authorized', user_id)
        return None

    @classmethod
    def sell_vehicle(cls, sale: Sale):
        cls.sales_list.append(sale)

    @classmethod
    def show_sale_list(cls):
        if len(cls.sales_list) == 0:
            print('No sales')
            input('Press <Enter> to continue')
        else:
            for index, sale in enumerate(cls.sales_list):
                _print_common_sale_info(sale)
                if index % 2 != 0:
                    _print_end_line_and_wait_for_enter()
                    _clear()
                else:
                    print('=============================================')

    @classmethod
    def show_sale_info(cls, license_plate):
        if len(cls.sales_list) == 0:
            print('No sales')
            input('Press <Enter> to continue')
        else:
            for sale in cls.sales_list:
                if sale.vehicle.license_plate == license_plate:
                    _print_common_sale_info(sale)
                    _print_truck_info_if_is_truck(sale.vehicle)
                    _print_bus_info_if_is_bus(sale.vehicle)
                    _print_van_info_if_is_van(sale.vehicle)
                    print('Proprietary information:')
                    print('NIF: ' + sale.vehicle.proprietary.nif)
                    if sale.vehicle.proprietary.name is not None:
                        print('Name: ' + sale.vehicle.proprietary.name)
                    if sale.vehicle.proprietary.surnames is not None:
                        print('Surnames: ' + sale.vehicle.proprietary.surnames)
                    if sale.vehicle.proprietary.business_name is not None:
                        print('Business name: ' + sale.vehicle.proprietary.business_name)
                    _print_end_line_and_wait_for_enter()

    @classmethod
    def get_sale_vehicle(cls, license_plate):
        for sale in cls.sales_list:
            if sale.vehicle.license_plate == license_plate:
                return sale.vehicle
        logging.error('Sale not found for plate license %s', license_plate)

    @classmethod
    def add_proprietary(cls, proprietary: Proprietary, license_plate):
        for vehicle in cls.vehicle_list:
            if vehicle.license_plate == license_plate:
                vehicle.proprietary = proprietary

    @classmethod
    def exist_vehicle(cls, license_plate):
        for elem in cls.vehicle_list:
            if elem.license_plate == license_plate:
                return True
        return False

    @classmethod
    def exist_vehicle_by_register_number(cls, register_number):
        for elem in cls.vehicle_list:
            if elem.get_register_number() == register_number:
                return True
        return False

    @classmethod
    def exist_user(cls, user_id):
        for elem in cls.user_list:
            if elem.get_user_code() == user_id:
                return True
        return False

    @classmethod
    def exist_sale(cls, license_plate):
        for sale in cls.sales_list:
            if sale.vehicle.license_plate == license_plate:
                return True
        return False

    @classmethod
    def exist_any_user(cls):
        user_request = requests.get("%s/users" % URL)
        if user_request.status_code == 200:
            user_request = user_request.json()
            if len(user_request) > 0:
                return True
            else:
                return False
        else:
            raise BackEndException("Cannot connect with backend")
