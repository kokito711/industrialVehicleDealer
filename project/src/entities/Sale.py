from datetime import datetime

from project.src.entities.Vehicle import Vehicle


class Sale():
    """
    Esta clase contiene un atributo de tipo vehículo y otro que se inicializa mediante un método. Su constructor recibe
     como parámetro un objeto de tipo vehículo
    """

    def __init__(self, vehicle: Vehicle):
        self.vehicle = vehicle
        self.sale_date = datetime.now().strftime('dd/MM/yyyy')
