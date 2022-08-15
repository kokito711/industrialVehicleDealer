import logging
from os import system, name

from singleton_decorator import singleton

from project.src.entities.Bus import Bus
from project.src.entities.Proprietary import Proprietary
from project.src.entities.Sale import Sale
from project.src.entities.Truck import Truck
from project.src.entities.User import User
from project.src.entities.Van import Van
from project.src.entities.Vehicle import Vehicle


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


@singleton
class VehicleDealer:
    """
    Esta clase utiliza un patrón de diseño singleton.
    Contiene 3 atributos; son List de tipos usuario, vehículo y venta.
    Estas listas almacenarán todos los datos del concesionario.
    """

    def __init__(self):
        self.user_list = list()
        self.sales_list = list()
        self.vehicle_list = list()

    def add_vehicle(self, vehicle: Vehicle):
        self.vehicle_list.append(vehicle)

    def remove_vehicle(self, register_number):
        for index, vehicle in enumerate(self.vehicle_list):
            if vehicle.get_register_number() == register_number:
                self.vehicle_list.remove(index)
        logging.error('Vehicle with ID %s not found', register_number)

    def show_showroom_vehicle_info(self, register_number):
        vehicle = self.get_showroom_vehicle(register_number)
        if vehicle is not None:
            _print_common_vehicle_info(vehicle)
            _print_truck_info_if_is_truck(vehicle)
            _print_bus_info_if_is_bus(vehicle)
            _print_van_info_if_is_van(vehicle)
            _print_end_line_and_wait_for_enter()

    def get_vehicle_list(self):
        if len(self.vehicle_list) == 0:
            print('No vehicles in showroom')
            input('Press <Enter> to continue')
        else:
            for vehicle in self.vehicle_list:
                _print_common_vehicle_info(vehicle)
                _print_end_line_and_wait_for_enter()
                _clear()

    def get_showroom_vehicle(self, register_number):
        for vehicle in self.vehicle_list:
            if vehicle.get_register_number() == register_number:
                return vehicle
        logging.error('Vehicle with ID %s not found', register_number)

    def add_user(self, user: User):
        self.user_list.append(user)

    def delete_user(self, user_id):
        for index, user in enumerate(self.user_list):
            if user.get_user_code() == user_id:
                self.user_list.remove(index)
        logging.error('User with ID %s not found', user_id)

    def get_users_list(self):
        if len(self.user_list) == 0:
            print('No users')
            input('Press <Enter> to continue')
        else:
            for index, user in enumerate(self.user_list):
                _print_user_info(user)
                if index % 2 == 0:
                    _print_end_line_and_wait_for_enter()
                    _clear()
                else:
                    print('=============================================')

    def get_user_info(self, user_id):
        for user in self.user_list:
            if user.get_user_code() == user_id:
                _print_user_info(user)
                _print_end_line_and_wait_for_enter()

    def get_user(self, user_id):
        for user in self.user_list:
            if user.get_user_code() == user_id:
                return user
        logging.error('User with ID %s not found', user_id)

    def sell_vehicle(self, sale: Sale):
        self.sales_list.append(sale)

    def show_sale_list(self):
        if len(self.sales_list) == 0:
            print('No sales')
            input('Press <Enter> to continue')
        else:
            for index, sale in enumerate(self.sales_list):
                _print_common_sale_info(sale)
                if index % 2 == 0:
                    _print_end_line_and_wait_for_enter()
                    _clear()
                else:
                    print('=============================================')

    def show_sale_info(self, license_plate):
        if len(self.sales_list) == 0:
            print('No sales')
            input('Press <Enter> to continue')
        else:
            for sale in self.sales_list:
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

    def get_sale_vehicle(self, license_plate):
        for sale in self.sales_list:
            if sale.vehicle.license_plate == license_plate:
                return sale
        logging.error('Sale not found for plate license %s', license_plate)

    def add_proprietary(self, proprietary: Proprietary, license_plate):
        for vehicle in self.vehicle_list:
            if vehicle.license_plate() == license_plate:
                vehicle.proprietary = proprietary

    def exist_vehicle(self, vehicle: Vehicle):
        for elem in self.vehicle_list:
            if elem == vehicle:
                return True
        return False

    def exist_user(self, user: User):
        for elem in self.user_list:
            if elem == user:
                return True
        return False

    def exist_sale(self, license_plate):
        for sale in self.sales_list:
            if sale.vehicle.license_plate == license_plate:
                return True
        return False
