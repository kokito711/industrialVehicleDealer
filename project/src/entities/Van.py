from datetime import datetime

from project.src.entities import Vehicle


class Van(Vehicle):
    """
    Esta clase define los atributos de los objetos de tipo Furgoneta y hereda los de tipo vehículo.
    """

    def __init__(self, load_volume, load_longitude, license_plate, brand, model,
                 color, build_date: datetime, kilometers, observations=None):
        super(Van, self).__init__(license_plate, brand, model, color, build_date, kilometers, observations)
        self.load_volume = load_volume
        self.load_longitude = load_longitude
