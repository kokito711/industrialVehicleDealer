import datetime
from unittest import TestCase

from project.src.entities.Bus import Bus
from project.src.entities.Truck import Truck
from project.src.entities.Van import Van
from project.src.entities.Video import Video
from project.src.service.VehicleDealer import VehicleDealer


def _create_truck():
    return Truck(10476, 18200, 6, '7700EIZ', 'Renault', 'T 520 HIGHCAB T4X2 X-LOW E6', 'Blanco',
                 datetime.datetime.strptime('02122015', '%d%m%Y').date(), 25)


def _create_van():
    return Van(5, 4963, '7700EIZ', 'Citroën', 'Jumper 30 L1 H1', 'Blanco',
               datetime.datetime.strptime('02122015', '%d%m%Y').date(), 15)


def _create_bus():
    return Bus(191, Video.NO, 12, '7700EIZ', 'Mercedes Benz', 'Capacity L', 'Blanco',
               datetime.datetime.strptime('02122015', '%d%m%Y').date(), 10)


def _initialize_vehicle_dealer():
    vehicle_dealer: VehicleDealer = VehicleDealer()
    if len(vehicle_dealer.vehicle_list) != 0:
        vehicle_dealer.vehicle_list = list()
    if len(vehicle_dealer.user_list) != 0:
        vehicle_dealer.user_list = list()
    if len(vehicle_dealer.sales_list) != 0:
        vehicle_dealer.sales_list = list()
    return vehicle_dealer


class TestVehicleDealer(TestCase):

    def test_vehicle_dealer_lists_correctly_initialized(self):
        vehicle_dealer = _initialize_vehicle_dealer()
        self.assertIsNotNone(vehicle_dealer.vehicle_list)
        self.assertIsNotNone(vehicle_dealer.user_list)
        self.assertIsNotNone(vehicle_dealer.sales_list)
        self.assertEqual(len(vehicle_dealer.vehicle_list), 0)
        self.assertEqual(len(vehicle_dealer.user_list), 0)
        self.assertEqual(len(vehicle_dealer.sales_list), 0)

    def test_add_truck(self):
        vehicle_dealer = _initialize_vehicle_dealer()
        vehicle = _create_truck()
        vehicle_dealer.vehicle_list.append(vehicle)

        self.assertEqual(len(vehicle_dealer.vehicle_list), 1)
        self.assertEqual(vehicle_dealer.vehicle_list[0], vehicle)

    def test_add_van(self):
        vehicle_dealer = _initialize_vehicle_dealer()
        vehicle = _create_van()
        vehicle_dealer.vehicle_list.append(vehicle)

        self.assertEqual(len(vehicle_dealer.vehicle_list), 1)
        self.assertEqual(vehicle_dealer.vehicle_list[0], vehicle)

    def test_add_bus(self):
        vehicle_dealer = _initialize_vehicle_dealer()
        vehicle = _create_bus()
        vehicle_dealer.vehicle_list.append(vehicle)

        self.assertEqual(len(vehicle_dealer.vehicle_list), 1)
        self.assertEqual(vehicle_dealer.vehicle_list[0], vehicle)

    def test_remove_vehicle(self):
        vehicle_dealer = _initialize_vehicle_dealer()
        vehicle = _create_van()

        vehicle_dealer.remove_vehicle(vehicle.get_register_number())

        self.assertTrue(len(vehicle_dealer.vehicle_list) == 0)
