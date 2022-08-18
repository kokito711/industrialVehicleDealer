import logging
from datetime import datetime

from project.src.entities import Maintenance, Proprietary


class Vehicle:
    """
    Esta clase tiene un atributo de tipo Array List de objetos de tipo mantenimiento y un atributo de tipo propietario, 
    a parte de estos atributos contiene otros de tipos “comunes”.
    """

    def __init__(self, license_plate, brand, model, color, build_date: datetime.date, kilometers, observations=None):
        date = datetime.now()

        if observations is None:
            observations = list()

        self.__register_number = date.strftime('ddMMyyyyHHmmss')
        self.license_plate = license_plate
        self.brand = brand
        self.model = model
        self.color = color
        self.buy_date = date
        self.build_date = build_date
        self.kilometers = kilometers
        self.observations = observations
        self.maintenance = list()
        self.proprietary = None

    def get_register_number(self):
        return self.__register_number

    def get_buy_date(self):
        return self.buy_date.strftime('dd/MM/yyyy')

    def get_build_date(self):
        return self.build_date.strftime('dd/MM/yyyy')

    def add_maintenance(self, maintenance: Maintenance):
        self.maintenance.append(maintenance)

    def add_proprietary(self, proprietary: Proprietary):
        self.proprietary = proprietary

    def print_maintenance_list(self):
        if len(self.maintenance) == 0:
            logging.info('Maintenance list is empty')
        else:
            counter = 0
            for elem in self.maintenance:
                logging.info('=============================================\n Maintenance: '
                             + elem.get_maintenance_date() + '\n Maintenance date: ' + elem.get_maintenance_date()
                             + '\n Kilometers: ' + elem.kilometers + '\n Price: ' + elem.price + '\n Done work: '
                             + elem.done_work + '\n =============================================')
                counter = counter + 1
                if counter == 2:
                    input('Press <Enter> to continue')
                    counter = 0
