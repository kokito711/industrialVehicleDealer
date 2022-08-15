import datetime
from unittest import TestCase

from project.src.entities.Bus import Bus
from project.src.entities.Truck import Truck
from project.src.entities.Van import Van
from project.src.entities.Video import Video
from project.src.service.VehicleDealer import VehicleDealer


def _initialize_vehicle_dealer():
    vehicle_dealer: VehicleDealer = VehicleDealer()
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
        vehicle = Truck(10476, 18200, 6, '7700EIZ', 'Renault', 'T 520 HIGHCAB T4X2 X-LOW E6', 'Blanco',
                        datetime.datetime.strptime('02122015', '%d%m%Y').date(), 25)
        vehicle_dealer.vehicle_list.append(vehicle)

        self.assertEqual(len(vehicle_dealer.vehicle_list), 1)
        self.assertEqual(vehicle_dealer.vehicle_list[0], vehicle)

    def test_add_van(self):
        vehicle_dealer = _initialize_vehicle_dealer()
        vehicle = Van(5, 4963, '7700EIZ', 'Citroën', 'Jumper 30 L1 H1', 'Blanco',
                      datetime.datetime.strptime('02122015', '%d%m%Y').date(), 15)
        vehicle_dealer.vehicle_list.append(vehicle)

        self.assertEqual(len(vehicle_dealer.vehicle_list), 1)
        self.assertEqual(vehicle_dealer.vehicle_list[0], vehicle)

    def test_add_bus(self):
        vehicle_dealer = _initialize_vehicle_dealer()
        vehicle = Bus(191, Video.NO, 12, '7700EIZ', 'Mercedes Benz', 'Capacity L', 'Blanco',
                      datetime.datetime.strptime('02122015', '%d%m%Y').date(), 10)
        vehicle_dealer.vehicle_list.append(vehicle)

        self.assertEqual(len(vehicle_dealer.vehicle_list), 1)
        self.assertEqual(vehicle_dealer.vehicle_list[0], vehicle)

    def test_remove_vehicle(self):
        self.fail()

    def test_show_showroom_vehicle_info(self):
        self.fail()

    def test_get_showroom_vehicle(self):
        self.fail()

    def test_add_user(self):
        self.fail()

    def test_delete_user(self):
        self.fail()

    def test_get_users_list(self):
        self.fail()

    def test_get_user_info(self):
        self.fail()

    def test_get_user(self):
        self.fail()

    def test_sell_vehicle(self):
        self.fail()

    def test_show_sale_list(self):
        self.fail()

    def test_show_sale_info(self):
        self.fail()

    def test_get_sale_vehicle(self):
        self.fail()

    def test_add_proprietary(self):
        self.fail()

    def test_exist_vehicle(self):
        self.fail()

    def test_exist_user(self):
        self.fail()

    def test_exist_sale(self):
        self.fail()
