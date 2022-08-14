import datetime


class Proprietary:
    pass


class Maintenance:
    pass


class Vehicle:
    """
    Esta clase tiene un atributo de tipo Array List de objetos de tipo mantenimiento y un atributo de tipo propietario, 
    a parte de estos atributos contiene otros de tipos “comunes”.
    """

    def __init__(self, register_number, license_plate, brand, model, color, buy_date: datetime, build_date: datetime,
                 kilometers, maintenance: list, proprietary: Proprietary, observations=None):
        self.register_number = register_number
        self.license_plate = license_plate
        self.brand = brand
        self.model = model
        self.color = color
        self.buy_date = buy_date
        self.build_date = build_date
        self.kilometers = kilometers
        self.observations = observations
        self.maintenance = maintenance
        self.proprietary = proprietary
