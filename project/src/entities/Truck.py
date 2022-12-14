import datetime

from project.src.entities.Vehicle import Vehicle


class Truck(Vehicle):
    """
    Esta clase define los atributos de los objetos de tipo camión y hereda los de tipo vehículo.
    """

    def __init__(self, tara, maximum_auth_charge, number_of_wheels, license_plate, brand, model,
                 color, build_date: datetime.date, kilometers, observations=None):
        super(Truck, self).__init__(license_plate, brand, model, color, build_date, kilometers, observations)
        self.tara = tara
        self.maximum_auth_charge = maximum_auth_charge
        self.number_of_wheels = number_of_wheels
