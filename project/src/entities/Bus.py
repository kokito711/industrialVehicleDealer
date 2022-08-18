from datetime import datetime

from project.src.entities import Vehicle, Video


class Bus(Vehicle.Vehicle):
    """
    Esta clase define los atributos de los objetos de tipo Bus y hereda los de tipo vehículo.
    """

    def __init__(self, passenger_number, video: Video, number_of_wheels, license_plate, brand, model,
                 color, build_date: datetime.date, kilometers, observations=None):
        super(Bus, self).__init__(license_plate, brand, model, color, build_date, kilometers, observations)
        self.passenger_number = passenger_number
        self.video = video
        self.number_of_wheels = number_of_wheels
